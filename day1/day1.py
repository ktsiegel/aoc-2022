from sys import argv


def main(filename):
    # Read the input file
    with open(filename, "r") as f:
        input = f.read()

    # Parse the input
    input = input.split("\n\n")

    max_cals = 0
    for elf in input:
        calories = sum([int(x) for x in elf.split("\n")])
        max_cals = max(calories, max_cals)
    print(max_cals)


if __name__ == "__main__":
    main(argv[1])
