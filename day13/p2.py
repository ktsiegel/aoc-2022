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


# -1 indicates first < second, 1 first > second, 0 indicates unknown sort
def compare(first, second):
    if type(first) == int and type(second) == int:
        if first < second:
            return -1
        elif first == second:
            return 0
        else:
            return 1
    elif type(first) == int:
        return compare([first], second)
    elif type(second) == int:
        return compare(first, [second])
    else:
        # both are lists
        for i in range(min(len(first), len(second))):
            comp = compare(first[i], second[i])
            if comp != 0:
                return comp
        if len(first) > len(second):
            return 1
        elif len(first) < len(second):
            return -1
        return 0


def main(filename):
    # Read the input file
    with open(filename, "r") as f:
        input = [x.strip() for x in f.readlines()]

    dividers = ["[[2]]", "[[6]]"]
    input += dividers
    packets = []
    for l in input:
        if l != "":
            packet = parse_nested_array(l)
            if len(packets) == 0:
                packets.append(packet)
            else:
                inserted = False
                for i in range(len(packets)):
                    if compare(packets[i], packet) == 1:
                        packets.insert(i, packet)
                        inserted = True
                        break
                if not inserted:
                    packets.append(packet)

    decoder = 1
    for d in dividers:
        decoder *= (packets.index(parse_nested_array(d))+1)
    print(decoder)


if __name__ == "__main__":
    main(argv[1])
