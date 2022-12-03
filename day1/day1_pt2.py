from sys import argv


def main(filename):
    # Read the input file
    with open(filename, "r") as f:
        input = f.read()

    # Parse the input
    input = input.split("\n\n")

    max_cals = []
    for elf in input:
        calories = sum([int(x) for x in elf.split("\n")])
        if len(max_cals) < 3:
            max_cals.append(calories)
            max_cals.sort()
        elif calories > max_cals[0]:
            max_cals[0] = calories
            max_cals.sort()
    print(sum(max_cals))


if __name__ == "__main__":
    main(argv[1])
