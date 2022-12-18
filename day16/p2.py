from sys import argv


def main(filename):
    # Read the input file
    with open(filename, "r") as f:
        input = [x.strip() for x in f.readlines()]

if __name__ == "__main__":
    main(argv[1])

        