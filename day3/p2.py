from sys import argv


def get_value(c):
    val_str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return val_str.index(c) + 1


def main(filename):
    # Read the input file
    with open(filename, "r") as f:
        input = [x.strip() for x in f.readlines()]

    total = 0

    i = 0
    while i < len(input):
        first = input[i]
        second = input[i+1]
        third = input[i+2]

        overlap = set(first).intersection(set(second)
                                          ).intersection(set(third)).pop()
        total += get_value(overlap)

        i += 3

    print(total)


if __name__ == "__main__":
    main(argv[1])
