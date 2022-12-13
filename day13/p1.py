from sys import argv


def parse_nested_array(line):
    if line[0] != "[":
        return int(line)
    arr = []
    accum = ""
    depth = 0
    for i in range(1, len(line) - 1):
        if line[i] == "," and depth == 0:
            arr.append(parse_nested_array(accum))
            accum = ""
        else:
            accum = accum + line[i]
            if line[i] == "[":
                depth += 1
            elif line[i] == "]":
                depth -= 1
    if accum != "":
        arr.append(parse_nested_array(accum))

    return arr


# 1 indicates right order, -1 indicates wrong, 0 indicates unknown
def right_order(first, second):
    if type(first) == int and type(second) == int:
        if first < second:
            return 1
        elif first == second:
            return 0
        else:
            return -1
    elif type(first) == int:
        return right_order([first], second)
    elif type(second) == int:
        return right_order(first, [second])
    else:
        # both are lists
        for i in range(min(len(first), len(second))):
            comp = right_order(first[i], second[i])
            if comp != 0:
                return comp
        if len(first) > len(second):
            return -1
        elif len(first) < len(second):
            return 1
        return 0


def main(filename):
    # Read the input file
    with open(filename, "r") as f:
        input = [x.strip() for x in f.readlines()]

    i = 0
    count = 0
    while i < len(input):
        first = parse_nested_array(input[i])
        second = parse_nested_array(input[i + 1])
        if right_order(first, second) == 1:
            count += (i/3+1)

        i += 3

    print(count)


if __name__ == "__main__":
    main(argv[1])
