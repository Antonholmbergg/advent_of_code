# left lower
# right higer
# 0-99
# RXX / LXX xx is distance
# one per line
# starts at 50
# the password is the number of times the dial is left at 0


def main() -> None:
    n_times_at_0 = 0
    position = 50
    with open("01/input.txt", "r") as f:
        for line in f:
            direction = line[0]
            distance = int(line[1:])
            if direction == "R":
                position += distance
            else:
                position -= distance
            position %= 100
            if position == 0:
                n_times_at_0 += 1
    print(n_times_at_0)


if __name__ == "__main__":
    main()
