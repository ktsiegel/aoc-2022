from sys import argv
import os


defaultFileContent = """from sys import argv


def main(filename):
    # Read the input file
    with open(filename, "r") as f:
        input = f.read()

if __name__ == "__main__":
    main(argv[1])

        """


def main(day):
    os.mkdir("day{}".format(day))

    with open("day{}/p1.py".format(day), "w") as f:
        f.write(defaultFileContent)

    with open("day{}/p2.py".format(day), "w") as f:
        f.write(defaultFileContent)


if __name__ == "__main__":
    main(argv[1])
