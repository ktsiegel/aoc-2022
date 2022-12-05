from sys import argv

def parse_input_line(line):
    return [[int(x) for x in e.split('-')] for e in line.split(',')]

def get_overlap(first_elf, second_elf):
    begin = max(first_elf[0], second_elf[0])
    end = min(first_elf[1], second_elf[1])
    return (begin, end)

def main(filename):
    # Read the input file
    with open(filename, "r") as f:
        input = [x.strip() for x in f.readlines()]

    count = 0
    for i in input:
        [first_elf, second_elf] = parse_input_line(i)

        (begin, end) = get_overlap(first_elf, second_elf)
        if end >= begin:
            count += 1

    print(count)


if __name__ == "__main__":
    main(argv[1])

