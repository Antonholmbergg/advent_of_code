from pathlib import Path

import numpy as np
import numpy.typing as npt
from scipy.signal import convolve2d


def string_to_matrix(roll_positions: str) -> npt.NDArray:
    char_map = {"@": 1, ".": 0}
    return np.array([[char_map[x] for x in row] for row in roll_positions.split("\n")])


def count_moavable(roll_positions: str) -> int:
    roll_pos_matrix = string_to_matrix(roll_positions)
    # roll_pos_matrix = np.pad(roll_pos_matrix, 1)
    kernel = np.ones((3, 3))
    kernel[1, 1] = 0
    neighbour_sum = (
        convolve2d(roll_pos_matrix, kernel, mode="same", boundary="fill", fillvalue=0) < 4
    )
    # remove the locations that do not have a roll
    return np.multiply(neighbour_sum, roll_pos_matrix).sum()


def test_string_to_matrix() -> None:
    test_inp = "@.@.\n..@@"
    correct_output = np.array([[1, 0, 1, 0], [0, 0, 1, 1]])
    assert np.all(string_to_matrix(test_inp) == correct_output)


def test_task1() -> None:
    example_input = "..@@.@@@@.\n@@@.@.@.@@\n@@@@@.@.@@\n@.@@@@..@.\n@@.@@@@.@@\n.@@@@@@@.@\n.@.@.@.@@@\n@.@@@.@@@@\n.@@@@@@@@.\n@.@.@@@.@."
    example_output = 13
    assert count_moavable(example_input) == example_output


def main() -> None:
    with open(Path(__file__).parent / "input.txt") as f:
        print(count_moavable(f.read().rstrip("\n")))


if __name__ == "__main__":
    main()
