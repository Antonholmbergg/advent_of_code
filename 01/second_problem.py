# password method 0x434C49434B
# i.e. the number of times it passes 0 in total not just at the end of a turn


def main() -> None:
    n_times_at_0 = 0
    old_position = 50
    with open("01/input.txt", "r") as f:
        for line in f:
            direction = line[0]
            distance = int(line[1:])

            if direction == "R":
                new_position = old_position + distance
                new_position %= 100
                if (
                    new_position <= old_position
                ):  # if distance == 0: doesn't happen so dont need to account for it
                    n_times_at_0 += 1
                n_times_at_0 += distance // 100
            else:
                new_position = old_position - distance
                new_position %= 100
                if (
                    new_position <= old_position
                ):  # if distance == 0: doesn't happen so dont need to account for it
                    n_times_at_0 += 1
                n_times_at_0 += distance // 100
            old_position = new_position
            # if new_position == 0:
            # n_times_at_0 += 1
    print(n_times_at_0)


if __name__ == "__main__":
    main()
