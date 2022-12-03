from sys import argv
import os


defaultFileContent = """from sys import argv


def main(filename):
    # Read the input file
    with open(filename, "r") as f:
        input = [x.strip() for x in f.readlines()]

if __name__ == "__main__":
    main(argv[1])

        """


def main(day):
    os.mkdir("day{}".format(day))

    with open("day{}/p1.py".format(day), "w") as f:
        f.write(defaultFileContent.format("\"1.txt\""))

    with open("day{}/p2.py".format(day), "w") as f:
        f.write(defaultFileContent.format("\"2.txt\""))


if __name__ == "__main__":
    main(argv[1])
