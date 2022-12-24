from sys import argv
import time

def print_grid(grid, x, y):
    for i in range(len(grid)):
        s = ""
        for j in range(len(grid[i])):
            if i == x and j == y:
                s += "E"
            elif grid[i][j] == "#":
                s += "#"
            elif len(grid[i][j]) == 0:
                s += "."
            elif len(grid[i][j]) == 1:
                s += grid[i][j][0]
            else:
                s += str(len(grid[i][j]))
        print(s)
    print("\n")

def increment_grid_time(grid):
    next = []
    for i in range(len(grid)):
        row = []
        for j in range(len(grid[i])):
            occupants = grid[i][j]
            if occupants == "#":
                row.append("#")
            else:
                row.append([])
        next.append(row)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            occupants = grid[i][j]
            if occupants != "#":
                for occ in occupants:
                    if occ == ">":
                        if next[i][j+1] != "#":
                            next[i][j+1].append(occ)
                        else:
                            next[i][1].append(occ)
                    elif occ == "<":
                        if next[i][j-1] != "#":
                            next[i][j-1].append(occ)
                        else: 
                            next[i][len(grid[i])-2].append(occ)
                    elif occ == "^":
                        if next[i-1][j] != "#":
                            next[i-1][j].append(occ)
                        else:
                            next[len(grid)-2][j].append(occ)
                    elif occ == "v":
                        if next[i+1][j] != "#":
                            next[i+1][j].append(occ)
                        else:
                            next[1][j].append(occ)
    return next
            
def main(filename):
    start_time = time.time()
    # Read the input file
    with open(filename, "r") as f:
        input = [x.strip() for x in f.readlines()]

    grid = []
    for l in input:
        row = []
        for c in l:
            if c == ".":
                row.append([])
            elif c in "><^v":
                row.append([c])
            else:
                row.append(c)
        grid.append(row)

    initial_pos = (0, 1) # (x, y, time)
    finish = (len(grid)-1, len(grid[0])-2)

    (min_t, memoized_min_t) = solve(grid, (0,1,0), finish, False)

    (next_min_t, next_memoized_min_t) = solve(memoized_min_t, (finish[0], finish[1], 0), (0,1), True)

    (final_min_t, final_memoized_min_t) = solve(next_memoized_min_t, (initial_pos[0], initial_pos[1], 0), finish, False)

    print(min_t + next_min_t + final_min_t)
    print("--- %s seconds ---" % (time.time() - start_time))
    


def solve(grid, initial_pos, dest_pos, backwards):
    q = [initial_pos]
    
    memoized_grids = [grid]

    max_times = dict() # x, y, t % len(grid-2) -> t

    min_t = -1

    memo_div = (len(grid)-2)*(len(grid[0])-2)

    while len(q) > 0:
        # find all possible moves
        (x, y, t) = q.pop(-1)
        if t > min_t and min_t != -1:
            continue
        if x == dest_pos[0] and y == dest_pos[1]:
            if min_t == -1 or t < min_t:
                min_t = t

        memo_key = (x, y, t % memo_div)
        if memo_key not in max_times:
            max_times[memo_key] = t
        elif max_times[memo_key] < t+1:
            continue

        midx = (t+1) % memo_div
        if midx >= len(memoized_grids):
            mi = len(memoized_grids)
            while mi <= midx:
                memoized_grids.append(increment_grid_time(memoized_grids[mi-1]))
                mi += 1

        if not backwards:
            # move up
            if x > 0 and grid[x-1][y] != "#" and len(memoized_grids[midx][x-1][y]) == 0:
                q.append((x-1, y, t+1))

            # stay in place
            if len(memoized_grids[midx][x][y]) == 0:
                q.append((x, y, t+1))

            # move left
            if grid[x][y-1] != "#" and len(memoized_grids[midx][x][y-1]) == 0:
                q.append((x, y-1, t+1))

            # move down
            if x < len(grid)-1 and grid[x+1][y] != "#" and len(memoized_grids[midx][x+1][y]) == 0:
                q.append((x+1, y, t+1))

            # move right
            if grid[x][y+1] != "#" and len(memoized_grids[midx][x][y+1]) == 0:
                q.append((x, y+1, t+1))
        
        else:
            # move right
            if grid[x][y+1] != "#" and len(memoized_grids[midx][x][y+1]) == 0:
                q.append((x, y+1, t+1))

            # move down
            if x < len(grid)-1 and grid[x+1][y] != "#" and len(memoized_grids[midx][x+1][y]) == 0:
                q.append((x+1, y, t+1))

            # stay in place
            if len(memoized_grids[midx][x][y]) == 0:
                q.append((x, y, t+1))

            # move left
            if grid[x][y-1] != "#" and len(memoized_grids[midx][x][y-1]) == 0:
                q.append((x, y-1, t+1))

            # move up
            if x > 0 and grid[x-1][y] != "#" and len(memoized_grids[midx][x-1][y]) == 0:
                q.append((x-1, y, t+1))



    return (min_t, memoized_grids[min_t])

if __name__ == "__main__":
    main(argv[1])

        