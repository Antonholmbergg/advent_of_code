from dataclasses import dataclass
from pathlib import Path


@dataclass
class SafeDial:
    position: int = 50
    n_times_at_0: int = 0
    n_times_at_0_first_problem: int = 0

    def move_right(self, distance: int) -> None:
        extra_0 = 1 if (self.position + (distance % 100)) > 99 else 0
        times_passed_0_this_turn = distance // 100 + extra_0
        self.n_times_at_0 += times_passed_0_this_turn

        self.position += distance
        self.position %= 100

    def move_left(self, distance: int) -> None:
        extra_0 = 1 if (self.position - (distance % 100)) <= 0 else 0
        times_passed_0_this_turn = distance // 100 + extra_0
        self.n_times_at_0 += times_passed_0_this_turn

        self.position -= distance
        self.position %= 100

    def check_at_0(self) -> None:
        if self.position == 0:
            self.n_times_at_0_first_problem += 1


def main():
    safe_dial = SafeDial()
    with open(Path(__file__).parent / "input.txt") as f:
        for line in f:
            direction = line[0]
            distance = int(line[1:])
            if direction == "R":
                safe_dial.move_right(distance)
            else:
                safe_dial.move_left(distance)
            safe_dial.check_at_0()
    print(safe_dial)


def test_problem_1():
    test_sequence = "L68\nL30\nR48\nL5\nR60\nL55\nL1\nL99\nR14\nL82"
    expected_outcome = 3
    safe_dial = SafeDial()
    for line in test_sequence.split("\n"):
        direction = line[0]
        distance = int(line[1:])
        if direction == "R":
            safe_dial.move_right(distance)
        else:
            safe_dial.move_left(distance)
        safe_dial.check_at_0()
        print(safe_dial)


def test_problem_2():
    pass


if __name__ == "__main__":
    main()
