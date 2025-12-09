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