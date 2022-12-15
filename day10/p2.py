from sys import argv


def main(filename):
    # Read the input file
    with open(filename, "r") as f:
        input = [x.strip() for x in f.readlines()]

    crt = []
    for i in range(6):
        row = []
        for j in range(40):
            row.append(".")
        crt.append(row)

    cycle = 1
    x = 1
    for l in input:
        if (cycle-1)%40 >= x-1 and (cycle-1)%40 <= x+1:
            crt[int((cycle-1)/40)][(cycle-1)%40] = "#"

        cycle += 1

        if l == "noop":
            continue

        [addx, incr] = l.split(' ')

        if (cycle-1)%40 >= x-1 and (cycle-1)%40 <= x+1:
            crt[int((cycle-1)/40)][(cycle-1)%40] = "#"

        cycle += 1

        x += int(incr)
    printcrt(crt)

def printcrt(crt):
    for row in crt:
        print("".join(row))




if __name__ == "__main__":
    main(argv[1])

        