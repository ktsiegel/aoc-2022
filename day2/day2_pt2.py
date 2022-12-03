from sys import argv


def get_move(elf, result):
    if result == "X":
        # you lose
        if elf == "A":
            return "C"
        elif elf == "B":
            return "A"
        elif elf == "C":
            return "B"
    elif result == "Y":
        # you draw
        return elf
    elif result == "Z":
        # you win
        if elf == "A":
            return "B"
        elif elf == "B":
            return "C"
        elif elf == "C":
            return "A"


def get_result_score(result):
    if result == "X":
        return 0
    elif result == "Y":
        return 3
    elif result == "Z":
        return 6


def main(filename):
    # Read the input file
    with open(filename, "r") as f:
        input = f.read().strip().split("\n")

    score = 0
    for i in input:
        [elf, result] = i.split(' ')
        you = get_move(elf, result)
        if you == "A":
            score += 1
        elif you == "B":
            score += 2
        elif you == "C":
            score += 3

        score += get_result_score(result)

    print(score)


if __name__ == "__main__":
    main(argv[1])
