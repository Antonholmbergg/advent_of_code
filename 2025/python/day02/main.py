from pathlib import Path

def id_is_invalid_task1(id:int)->bool:
    str_id = str(id)
    n_digits = len(str_id)
    if str_id[:n_digits//2] == str_id[n_digits//2:]:
        return True
    else:
        return False


def _check_n_repeats(id: str, n_repeats):
    n_digits = len(id)
    if (n_digits % n_repeats) != 0:
        return False
    length_of_repeat = n_digits // n_repeats
    sections = [id[length_of_repeat*i:length_of_repeat*(i+1)] for i in range(n_repeats)]
    if all([sections[0] == section for section in sections[1:]]):
        return True
    else:
        return False
    

def id_is_invalid_task2(id:int)->bool:
    str_id = str(id)
    repeats_to_check = [2, 3, 5, 7]
    return any([_check_n_repeats(str_id, x) for x in repeats_to_check])


"""part 2



Now, an ID is invalid if it is made only of some sequence of digits repeated at least twice. So, 12341234 (1234 two times),
 123123123 (123 three times),
   1212121212 (12 five times),
     and 1111111 (1 seven times) are all invalid IDs.

From the same example as before:

11-22 still has two invalid IDs, 11 and 22.
95-115 now has two invalid IDs, 99 and 111.
998-1012 now has two invalid IDs, 999 and 1010.
1188511880-1188511890 still has one invalid ID, 1188511885.
222220-222224 still has one invalid ID, 222222.
1698522-1698528 still contains no invalid IDs.
446443-446449 still has one invalid ID, 446446.
38593856-38593862 still has one invalid ID, 38593859.
565653-565659 now has one invalid ID, 565656.
824824821-824824827 now has one invalid ID, 824824824.
2121212118-2121212124 now has one invalid ID, 2121212121.
Adding up all the invalid IDs in this example produces 4174379265.

"""

def main():
    with open(Path(__file__).parent / 'input.txt') as f:
        lines = f.read()
    product_id_ranges = lines.split(",")
    total_sum_task1 = 0
    total_sum_task2 = 0
    for product_id_range in product_id_ranges:
        start = int(product_id_range.split("-")[0])
        end = int(product_id_range.split("-")[1])
        product_id_range = range(start, end+1)
        invalid_ids_task1 = [x for x in product_id_range if id_is_invalid_task1(x)]
        total_sum_task1 += sum(invalid_ids_task1)
        invalid_ids_task2 = [x for x in product_id_range if id_is_invalid_task2(x)]
        total_sum_task2 += sum(invalid_ids_task2)
    print("total_sum_task1", total_sum_task1)
    print("total_sum_task2", total_sum_task2)

    
if __name__ == '__main__':
    main()