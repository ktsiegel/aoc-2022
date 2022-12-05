from sys import argv

def parseStacks(stackInputLines):
    stacks = []
    for i in range(len(stackInputLines)-1, -1, -1):
        row = [x.replace("]","").replace("[","") for x in stackInputLines[i].split("][")]
        for i in range(len(row)):
            if len(stacks) <= i:
                stacks.append([row[i]])
            else:
                stacks[i].append(row[i])

    return [filter(lambda x: x != "none", stack) for stack in stacks]

def main(filename):
    # Read the input file
    with open(filename, "r") as f:
        input = [x.replace("\n","") for x in f.readlines()]

    breakIndex = input.index("")
    stacks = parseStacks([x.replace("    ","[none]").replace(" ", "").strip() for x in input[:breakIndex-1]])
    instructions = input[breakIndex+1:]

    for instruction in instructions:
        parsed = instruction.split(" ")
        amount = int(parsed[1])
        fromIndex = int(parsed[3])-1
        toIndex = int(parsed[5])-1
        cutLine = len(stacks[fromIndex])-amount
        moving = stacks[fromIndex][cutLine:]
        stacks[fromIndex] = stacks[fromIndex][0:cutLine]
        stacks[toIndex]  = stacks[toIndex] + moving
        
    output = ""
    for s in stacks:
        if len(s) == 0:
            continue
        output += s[-1]
    print(output)
    

if __name__ == "__main__":
    main(argv[1])

        