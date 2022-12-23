from sys import argv

def checkNorth(elf, elves, dests):
    # check N, NE, or NW adjacent positions
    if (elf[0] - 1, elf[1]) not in elves and (elf[0]-1, elf[1]-1) not in elves and (elf[0]-1, elf[1]+1) not in elves:
        # move north one step
        dest = (elf[0]-1, elf[1])
        if dest not in dests:
            dests[dest] = []
        dests[dest].append(elf)
        return True
    return False

def checkSouth(elf, elves, dests):
    # check S, SE, or SW adjacent positions
    if (elf[0] + 1, elf[1]) not in elves and (elf[0]+1, elf[1]-1) not in elves and (elf[0]+1, elf[1]+1) not in elves:
        # move south one step
        dest = (elf[0]+1, elf[1])
        if dest not in dests:
            dests[dest] = []
        dests[dest].append(elf)
        return True
    return False

def checkWest(elf, elves, dests):
    # check W, NW, or SW adjacent positions
    if (elf[0], elf[1] - 1) not in elves and (elf[0]-1, elf[1]-1) not in elves and (elf[0]+1, elf[1]-1) not in elves:
        # move west one step
        dest = (elf[0], elf[1]-1)
        if dest not in dests:
            dests[dest] = []
        dests[dest].append(elf)
        return True
    return False

def checkEast(elf, elves, dests):
    # check E, NE, or SE adjacent positions
    if (elf[0], elf[1] + 1) not in elves and (elf[0]-1, elf[1]+1) not in elves and (elf[0]+1, elf[1]+1) not in elves:
        # move east one step
        dest = (elf[0], elf[1]+1)
        if dest not in dests:
            dests[dest] = []
        dests[dest].append(elf)
        return True
    return False

def printElves(elves):
    maxrow = max([x[0] for x in elves])
    maxcol = max([x[1] for x in elves])
    minrow = min([x[0] for x in elves])
    mincol = min([x[1] for x in elves])

    for i in range(minrow, maxrow+1, 1):
        r = ""
        for j in range(mincol, maxcol+1, 1):
            if (i,j) in elves:
                r += "#"
            else:
                r += "."
        print(r)
    print("\n")

def main(filename):
    # Read the input file
    with open(filename, "r") as f:
        input = [x.strip() for x in f.readlines()]

    elves = set()
    for r in range(len(input)):
        for c in range(len(input[r])):
            if input[r][c] == "#":
                elves.add((r,c))
    printElves(elves)

    i = 0
    while True:
        dests = dict() # maps next destination to elves that want to move there
        newelves = set()
        for elf in elves:
            # calculate where elf is going
            hasElf = False
            for r in range(elf[0]-1, elf[0]+2, 1):
                for c in range(elf[1]-1, elf[1]+2, 1):
                    if (r != elf[0] or c != elf[1]) and (r,c) in elves:
                        hasElf = True
                        break
                if hasElf:
                    break
            if not hasElf:
                newelves.add(elf)
                continue
            if i % 4 == 0:
                if checkNorth(elf, elves, dests) or checkSouth(elf, elves, dests) or checkWest(elf, elves, dests) or checkEast(elf, elves, dests):
                    continue
                else:
                    newelves.add(elf)
            elif i % 4 == 1:
                if checkSouth(elf, elves, dests) or checkWest(elf, elves, dests) or checkEast(elf, elves, dests) or checkNorth(elf, elves, dests):
                    continue
                else:
                    newelves.add(elf)
            elif i % 4 == 2:
                if checkWest(elf, elves, dests) or checkEast(elf, elves, dests) or checkNorth(elf, elves, dests) or checkSouth(elf, elves, dests):
                    continue
                else:
                    newelves.add(elf)
            elif i % 4 == 3:
                if checkEast(elf, elves, dests) or checkNorth(elf, elves, dests) or checkSouth(elf, elves, dests) or checkWest(elf, elves, dests):
                    continue
                else:
                    newelves.add(elf)

        # move elves
        for dest in dests:
            # if there is only one elf that wants to move there, then move
            if len(dests[dest]) == 1:
                # elves.remove(dests[dest][0])
                newelves.add(dest)
            # otherwise don't move
            else:
                for d in dests[dest]:
                    newelves.add(d)
        i += 1

        if len(elves.intersection(newelves)) == len(elves):
            print(i)
            return
        elves = newelves


        # printElves(elves)
        # breakpoint()

    maxrow = max([x[0] for x in elves])
    maxcol = max([x[1] for x in elves])
    minrow = min([x[0] for x in elves])
    mincol = min([x[1] for x in elves])

    count = 0
    for i in range(minrow, maxrow+1, 1):
        for j in range(mincol, maxcol+1, 1):
            if (i,j) not in elves:
                count += 1
    print(count)
    



    

if __name__ == "__main__":
    main(argv[1])

        