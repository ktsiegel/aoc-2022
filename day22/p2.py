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
        
    print("ins", len(instructions))

    pos = (0, init_pos_col)
    dir = "R" # L, R, U, D

    print(len(grid))
    # each side is length 50

    iidx = 0
    while iidx < len(instructions):
        if type(instructions[iidx]) == int:
            stop = False
            b = False
            for i in range(instructions[iidx]):
                if stop:
                    break
                if dir == "R":
                    if pos[1]+1 < len(grid[0]) and grid[pos[0]][pos[1]+1] == ".":
                        pos = (pos[0], pos[1]+1)
                    elif pos[1]+1 == len(grid[0]) or grid[pos[0]][pos[1]+1] == " ":
                        # wrap around
                        if pos[0] < 50:
                            # goes row 149-row at the end
                            # direction flips to left
                            b = True
                            print(dir, pos)
                            poss_pos = (149-pos[0], 99)
                            if grid[poss_pos[0]][poss_pos[1]] == ".":
                                pos = poss_pos
                                dir = "L"
                            else:
                                stop = True
                            print(dir, pos)

                        elif pos[0] < 100:
                            # goes to the bottom of col 100+pos[0]-50
                            # direction flips to up
                            print(dir, pos)
                            b = True
                            poss_pos = (99, 100+pos[0]-50)
                            if grid[poss_pos[0]][poss_pos[1]] == ".": 
                                pos = poss_pos
                                dir = "U"
                            else:
                                stop = True
                            print(dir, pos)
                        elif pos[0] < 150:
                            # goes to the right of row 49-(pos[0]-100)
                            # direction flips to left
                            print(dir, pos)
                            b = True
                            poss_pos = (49-(pos[0]-100), 149)
                            if grid[poss_pos[0]][poss_pos[1]] == ".": 
                                pos = poss_pos
                                dir = "L"
                            else:
                                stop = True
                            print(dir, pos)

                        else:
                            # goes to the bottom of col 50+pos[0]-150
                            # direction flips to up
                            print(dir, pos)
                            b = True
                            poss_pos = (149, 50+pos[0]-150)
                            if grid[poss_pos[0]][poss_pos[1]] == ".": 
                                pos = poss_pos
                                dir = "U"
                            else:
                                stop = True
                            print(dir, pos)
                    else:
                        break
                elif dir == "L":
                    if pos[1]-1 >= 0 and grid[pos[0]][pos[1]-1] == ".":
                        pos = (pos[0], pos[1]-1)
                    elif pos[1]-1 < 0 or grid[pos[0]][pos[1]-1] == " ":
                        # wrap around
                        if pos[0] < 50:
                            print(dir, pos)
                            b = True
                            # goes to col 0, row 49-pos[0]+100
                            # direction flips to right
                            poss_pos = (49-pos[0]+100, 0)
                            if grid[poss_pos[0]][poss_pos[1]] == ".":
                                pos = poss_pos
                                dir = "R"
                            else:
                                stop = True
                            print(dir, pos)
                        elif pos[0] < 100:
                            # goes to row 100, col pos[0]-50
                            # direction flips to down
                            print(dir, pos)
                            b = True
                            poss_pos = (100, pos[0]-50)
                            if grid[poss_pos[0]][poss_pos[1]] == ".": 
                                pos = poss_pos
                                dir = "D"
                            else:
                                stop = True
                            print(dir, pos)
                        elif pos[0] < 150:
                            # goes to col 50, row 49-(pos[0]-100)
                            # direction flips to right
                            print(dir, pos)
                            b = True
                            poss_pos = (49-(pos[0]-100), 50)
                            if grid[poss_pos[0]][poss_pos[1]] == ".":
                                pos = poss_pos
                                dir = "R"
                            else:
                                stop = True
                            print(dir, pos)
                        else:
                            # goes to row 0, col 50+pos[0]-150
                            # direction flips to down
                            print(dir, pos)
                            b = True
                            poss_pos = (0, 50+pos[0]-150)
                            if grid[poss_pos[0]][poss_pos[1]] == ".":
                                pos = poss_pos
                                dir = "D"
                            else:
                                stop = True
                            print(dir, pos)
                    else:
                        break
                elif dir == "U":
                    if pos[0]-1 >= 0 and grid[pos[0]-1][pos[1]] == ".":
                        pos = (pos[0]-1, pos[1])
                    elif pos[0]-1 < 0 or grid[pos[0]-1][pos[1]] == " ":
                        # wrap around
                        if pos[1] < 50:
                            # goes to row 50+pos[1], col 50
                            # direction flips to right
                            print(dir, pos)
                            b = True
                            poss_pos = (50+pos[1], 50)
                            if grid[poss_pos[0]][poss_pos[1]] == ".":
                                pos = poss_pos
                                dir = "R"
                            else:
                                stop = True
                            print(dir, pos)
                        elif pos[1] < 100:
                            # goes to row pos[0]-50+150, col 0
                            # direction flips to right
                            print(dir, pos)
                            b = True
                            poss_pos = (pos[1]-50+150, 0)
                            if grid[poss_pos[0]][poss_pos[1]] == ".": 
                                pos = poss_pos
                                dir = "R"
                            else:
                                stop = True
                            print(dir, pos)
                        elif pos[1] < 150:
                            # goes to row 199, col pos[1]-100
                            # direction stays up
                            print(dir, pos)
                            b = True
                            poss_pos = (199, pos[1]-100)
                            if grid[poss_pos[0]][poss_pos[1]] == ".":
                                pos = poss_pos
                            else:
                                stop = True
                            print(dir, pos)
                        else:
                            raise Exception("oops")
                    else:
                        break
                elif dir == "D":
                    if pos[0]+1 < len(grid) and grid[pos[0]+1][pos[1]] == ".":
                        pos = (pos[0]+1, pos[1])
                    elif pos[0]+1 == len(grid) or grid[pos[0]+1][pos[1]] == " ":
                        # wrap around
                        if pos[1] < 50:
                            print(dir, pos)
                            b = True
                            # goes to row 0, col 100+pos[1]
                            # direction stays down
                            poss_pos = (0, 100+pos[1])
                            if grid[poss_pos[0]][poss_pos[1]] == ".":
                                pos = poss_pos
                            else:
                                stop = True
                            print(dir, pos)
                        elif pos[1] < 100:
                            # goes to row pos[1]-50+150, col 49
                            # direction changes to left
                            print(dir, pos)
                            b = True
                            poss_pos = (pos[1]-50+150, 49)
                            if grid[poss_pos[0]][poss_pos[1]] == ".":
                                pos = poss_pos
                                dir = "L"
                            else:
                                stop = True
                            print(dir, pos)
                        elif pos[1] < 150:
                            # goes to row pos[1]-100+50, col 99
                            # direction changes to left
                            print(dir, pos)
                            b = True
                            poss_pos = (pos[1]-100+50, 99)
                            if grid[poss_pos[0]][poss_pos[1]] == ".":
                                pos = poss_pos
                                dir = "L"
                            else:
                                stop = True
                            print(dir, pos)
                        else:
                            raise Exception("oops")
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

        # print(instructions[iidx])
        
        iidx += 1
        # if b:
            # for gi in range(len(grid)):
            #     g = grid[gi]
            #     s = ''.join(g)
            #     if gi == pos[0]:
            #         s = s[0:pos[1]] + "X" + s[pos[1]+1:]
            #     print(s)
            # print("\n")
            # breakpoint()
        b = False
        

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

        