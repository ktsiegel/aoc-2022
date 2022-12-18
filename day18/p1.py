from sys import argv


def main(filename):
    # Read the input file
    with open(filename, "r") as f:
        input = [[int(y) for y in x.strip().split(",")] for x in f.readlines()]

    total_sides = len(input) * 6

    rocks = set()
    for l in input:
        rocks.add((l[0], l[1], l[2]))

    for l in input:
        (i, j, k) = l
        poss = [(i+1, j, k), (i-1, j, k), (i, j+1, k),
                (i, j-1, k), (i, j, k+1), (i, j, k-1)]
        for p in poss:
            if p in rocks:
                total_sides -= 1

    print(total_sides)


if __name__ == "__main__":
    main(argv[1])
