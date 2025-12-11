# password method 0x434C49434B
# i.e. the number of times it passes 0 in total not just at the end of a turn
from dataclasses import dataclass


def _main() -> None:
    n_times_at_0 = 0
    n_times_at_0_first_problem = 0

    old_position = 50
    with open("01/input.txt", "r") as f:
        for line in f:
            direction = line[0]
            distance = int(line[1:])
            if distance == 0:  # doesn't happen so dont need to account for it
                print(distance)
            n_times_at_0 += distance // 100

            if direction == "R":
                new_position = old_position + distance
                new_position %= 100
                if new_position < old_position:
                    n_times_at_0 += 1
            else:
                new_position = old_position - distance
                new_position %= 100
                if new_position > old_position:
                    n_times_at_0 += 1
            old_position = new_position
            if new_position == 0:
                n_times_at_0_first_problem += 1
    print(n_times_at_0)
    print(n_times_at_0_first_problem)


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
    with open("01/input.txt", "r") as f:
        for line in f:
            direction = line[0]
            distance = int(line[1:])
            if direction == "R":
                safe_dial.move_right(distance)
            else:
                safe_dial.move_left(distance)
            safe_dial.check_at_0()
    print(safe_dial)


if __name__ == "__main__":
    main()
