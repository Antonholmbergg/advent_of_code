from pathlib import Path

import pytest


def _find_max_and_ind(list_of_digits: list[int]) -> tuple[int, int]:
    max_digit = -1
    max_ind = 0
    for i, digit in enumerate(list_of_digits):
        if digit > max_digit:
            max_digit = digit
            max_ind = i
    return max_digit, max_ind


def find_max_in_bank(list_of_digits: list[int], n_batteries: int) -> int:
    if n_batteries > 1:
        n_batteries -= 1
        value, ind = _find_max_and_ind(list_of_digits=list_of_digits[:-n_batteries])
        return value * (10**n_batteries) + find_max_in_bank(list_of_digits[ind + 1 :], n_batteries)
    else:
        value, _ = _find_max_and_ind(list_of_digits=list_of_digits)
        return value  # *(10**0)


example_input = ["987654321111111", "811111111111119", "234234234234278", "818181911112111"]
answers_per_row_task_1 = [98, 89, 78, 92]


@pytest.mark.parametrize(("input", "output"), zip(example_input, answers_per_row_task_1))
def test_max_in_bank_task_1(input, output):
    assert find_max_in_bank([int(digit) for digit in input], n_batteries=2) == output


answers_per_row_task_2 = [987654321111, 811111111119, 434234234278, 888911112111]


@pytest.mark.parametrize(("input", "output"), zip(example_input, answers_per_row_task_2))
def test_max_in_bank_task_2(input, output):
    assert find_max_in_bank([int(digit) for digit in input], n_batteries=12) == output


def main():
    first_total = 0
    second_total = 0
    with open(Path(__file__).parent / "input.txt") as f:
        for line in f:
            list_of_digits = [int(digit) for digit in line.strip("\n")]
            first_total += find_max_in_bank(list_of_digits=list_of_digits, n_batteries=2)
            second_total += find_max_in_bank(list_of_digits=list_of_digits, n_batteries=12)
    print("first_total", first_total)
    print("second_total", second_total)


if __name__ == "__main__":
    main()
