from sys import argv


def get_value(c):
    val_str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return val_str.index(c) + 1


def main(filename):
    # Read the input file
    with open(filename, "r") as f:
        input = f.readlines()

    total = 0
    for i in input:
        first_half = set(i[:len(i)//2])
        second_half = set(i[len(i)//2:])
        overlap = first_half.intersection(second_half)
        total += get_value(overlap.pop())

    print(total)


if __name__ == "__main__":
    main(argv[1])
