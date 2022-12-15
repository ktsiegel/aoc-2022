from sys import argv


def main(filename):
    # Read the input file
    with open(filename, "r") as f:
        input = [x.strip() for x in f.readlines()]

    cycle = 0
    x = 1
    strength = 0
    for l in input:
        cycle += 1
        if (cycle - 20) % 40 == 0:
            strength += cycle * x


        if l == "noop":
            continue

        [addx, incr] = l.split(' ')
        cycle += 1
        if (cycle - 20) % 40 == 0:
            strength += cycle * x
        
        x += int(incr)
    print(strength)




if __name__ == "__main__":
    main(argv[1])

        