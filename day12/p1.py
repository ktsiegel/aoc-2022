from sys import argv


def main(filename):
    # Read the input file
    with open(filename, "r") as f:
        input = [x.strip() for x in f.readlines()]

    grid = []
    for i in range(len(input)):
        l = input[i]
        row = []
        for c in range(len(l)):
            item = l[c]
            if item == "S":
                item = "a"
                start = [i, c]
            elif item == "E":
                item = "z"
                end = [i, c]
            row.append([item, -1])
        grid.append(row)

    grid[start[0]][start[1]][1] = 0

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    bfs = [start]
    while len(bfs) > 0:
        curr = bfs.pop(0)
        top = [curr[0], curr[1]-1]
        bottom = [curr[0], curr[1]+1]
        left = [curr[0]-1, curr[1]]
        right = [curr[0]+1, curr[1]]

        curr_val = grid[curr[0]][curr[1]][0]
        for poss in [top, bottom, left, right]:
            if poss[0] < 0 or poss[0] >= len(grid) or poss[1] < 0 or poss[1] >= len(grid[0]):
                continue
            poss_val = grid[poss[0]][poss[1]][0]
            if alphabet.index(curr_val) + 1 >= alphabet.index(poss_val):
                path_len = grid[curr[0]][curr[1]][1]+1
                if grid[poss[0]][poss[1]][1] > path_len or grid[poss[0]][poss[1]][1] == -1:
                    # can move here, haven't visited yet
                    grid[poss[0]][poss[1]][1] = path_len
                    bfs.append(poss)

    print(grid[end[0]][end[1]][1])


if __name__ == "__main__":
    main(argv[1])
