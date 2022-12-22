from sys import argv


def main(filename):
    # Read the input file
    with open(filename, "r") as f:
        input = [x.replace("\n","") for x in f.readlines()]

    maxlen = 0
    for i in range(len(input)-2):
        l = input[i]
        maxlen = max(maxlen, len(l))

    code = input[-1]

    # Create a 2D array of the input
    grid = []
    for j in range(len(input)-2):
        l = input[j]
        row = []
        for i in range(maxlen):
            if i >= len(l):
                c = " "
            else:
                c = l[i]
            row.append(c)
        grid.append(row)
    
    # for l in grid:
    #     print(''.join(l))

    init_pos_col = 0
    for col in range(len(grid[0])):
        if grid[0][col] != " ":
            init_pos_col = col
            break
    # print(init_pos_col)
    # print(code)

    instructions = []

    i = 0
    while i < len(code):
        digit = ""
        while i < len(code) and code[i].isdigit():
            digit += code[i]
            i+=1
        instructions.append(int(digit))
        if i == len(code):
            break
        dir = ""
        while i < len(code) and  not code[i].isdigit():
            dir += code[i]
            i += 1
        instructions.append(dir)
        
    print(instructions)

    pos = (0, init_pos_col)
    dir = "R" # L, R, U, D

    iidx = 0
    while iidx < len(instructions):
        if type(instructions[iidx]) == int:
            if dir == "R":
                for i in range(instructions[iidx]):
                    if pos[1]+1 < len(grid[0]) and grid[pos[0]][pos[1]+1] == ".":
                        pos = (pos[0], pos[1]+1)
                    elif pos[1]+1 == len(grid[0]) or grid[pos[0]][pos[1]+1] == " ":
                        # wrap around
                        for wrapi in range(0, len(grid[0])):
                            if grid[pos[0]][wrapi] != " ":
                                poss_pos = (pos[0], wrapi)
                                break
                        if grid[poss_pos[0]][poss_pos[1]] == ".": 
                            pos = poss_pos
                        else:
                            break
                    else:
                        break
            elif dir == "L":
                for i in range(instructions[iidx]):
                    if pos[1]-1 >= 0 and grid[pos[0]][pos[1]-1] == ".":
                        pos = (pos[0], pos[1]-1)
                    elif pos[1]-1 < 0 or grid[pos[0]][pos[1]-1] == " ":
                        # wrap around
                        for wrapi in range(len(grid[0])-1, -1, -1):
                            if grid[pos[0]][wrapi] != " ":
                                poss_pos = (pos[0], wrapi)
                                break
                        if grid[poss_pos[0]][poss_pos[1]] == ".": 
                            pos = poss_pos
                        else:
                            break
                    else:
                        break
            elif dir == "U":
                for i in range(instructions[iidx]):
                    if pos[0]-1 >= 0 and grid[pos[0]-1][pos[1]] == ".":
                        pos = (pos[0]-1, pos[1])
                    elif pos[0]-1 < 0 or grid[pos[0]-1][pos[1]] == " ":
                        # wrap around
                        for wrapi in range(len(grid)-1, -1, -1):
                            if grid[wrapi][pos[1]] != " ":
                                poss_pos = (wrapi, pos[1])
                                break
                        if grid[poss_pos[0]][poss_pos[1]] == ".": 
                            pos = poss_pos
                        else:
                            break
                    else:
                        break
            elif dir == "D":
                for i in range(instructions[iidx]):
                    if pos[0]+1 < len(grid) and grid[pos[0]+1][pos[1]] == ".":
                        pos = (pos[0]+1, pos[1])
                    elif pos[0]+1 == len(grid) or grid[pos[0]+1][pos[1]] == " ":
                        # wrap around
                        for wrapi in range(0, len(grid)):
                            if grid[wrapi][pos[1]] != " ":
                                poss_pos = (wrapi, pos[1])
                                break
                        if grid[poss_pos[0]][poss_pos[1]] == ".": 
                            pos = poss_pos
                        else:
                            break
                    else:
                        break
            else:
                raise Exception("Invalid direction")

        else:
            if instructions[iidx] == "R":
                if dir == "R":
                    dir = "D"
                elif dir == "L":
                    dir = "U"
                elif dir == "U":
                    dir = "R"
                elif dir == "D":
                    dir = "L"
                else:
                    raise Exception("Invalid direction")
            elif instructions[iidx] == "L":
                if dir == "R":
                    dir = "U"
                elif dir == "L":
                    dir = "D"
                elif dir == "U":
                    dir = "L"
                elif dir == "D":
                    dir = "R"
                else:
                    raise Exception("Invalid direction")
            else:
                raise Exception("Invalid direction")

        # for gi in range(len(grid)):
        #     g = grid[gi]
        #     s = ''.join(g)
        #     if gi == pos[0]:
        #         s = s[0:pos[1]] + "X" + s[pos[1]+1:]
        #     print(s)
        # print("\n")
        iidx += 1

    facing = 0
    if dir == "D":
        facing = 1
    elif dir == "L":
        facing = 2
    elif dir == "U":
        facing = 3
    print(1000*(pos[0]+1) + 4*(pos[1]+1)+facing)
    print(pos, dir)





if __name__ == "__main__":
    main(argv[1])

        