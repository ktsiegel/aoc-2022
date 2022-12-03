from sys import argv


def game_result(elf, raw_you):
    # 0 if loss, 1 if draw, 2 if win
    you = "A"
    if raw_you == "Y":
        you = "B"
    if raw_you == "Z":
        you = "C"

    if elf == you:
        return 1

    if (elf == "A" and you == "B") or (elf == "B" and you == "C") or (elf == "C" and you == "A"):
        return 2
    return 0


def main(filename):
    # Read the input file
    with open(filename, "r") as f:
        input = f.read().strip().split("\n")

    score = 0
    for i in input:
        [elf, you] = i.split(' ')
        if you == "X":
            score += 1
        elif you == "Y":
            score += 2
        elif you == "Z":
            score += 3

        score += game_result(elf, you) * 3

    print(score)


if __name__ == "__main__":
    main(argv[1])
