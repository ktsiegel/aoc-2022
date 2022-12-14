from sys import argv


def main(filename):
    # Read the input file
    with open(filename, "r") as f:
        input = [[[int(z) for z in y.split(",")] for y in x.strip().split(" -> ")]
                 for x in f.readlines()]

    print(input)

    rocks = set()
    horiz = set()
    for rock in input:
        for i in range(len(rock)-1):
            start = rock[i]
            end = rock[i+1]
            if start[0] != end[0] and start[1] != end[1]:
                raise Exception("oops")
            if start[0] == end[0]:
                curr = min(start[1], end[1])
                dest = max(start[1], end[1])
                horiz.add(start[0])
                while curr <= dest:
                    rocks.add((start[0], curr))
                    curr += 1
            elif start[1] == end[1]:
                curr = min(start[0], end[0])
                dest = max(start[0], end[0])
                while curr <= dest:
                    horiz.add(curr)
                    rocks.add((curr, start[1]))
                    curr += 1
            else:
                raise Exception("oops 2")

    max_horiz = max(horiz)
    min_horiz = min(horiz)

    init_rock_count = len(rocks)
    while True:
        # rock drops from col 500
        # get the vertical most rock in that column
        max_rock = None
        for r in rocks:
            if r[0] == 500:
                if max_rock is None or r[1] < max_rock[1]:
                    max_rock = r
        if max_rock is None:
            break

        new_rock_pos = (max_rock[0], max_rock[1]-1)
        moved = True
        while moved:
            (new_rock_pos, moved) = move_down(rocks, new_rock_pos)
            if new_rock_pos[0] > max_horiz or new_rock_pos[0] < min_horiz:
                # fell off
                print(len(rocks)-init_rock_count)
                return

        rocks.add(new_rock_pos)


def move_down(rocks, new_rock_pos):
    new_rock_pos_down = (new_rock_pos[0], new_rock_pos[1]+1)
    if new_rock_pos_down not in rocks:
        # falling down
        return new_rock_pos_down, True
    # move diagonally one step down and to the left
    new_rock_pos_left = (new_rock_pos[0]-1, new_rock_pos[1]+1)
    if new_rock_pos_left not in rocks:
        # falling down and to the left
        return new_rock_pos_left, True
    new_rock_pos_right = (new_rock_pos[0]+1, new_rock_pos[1]+1)
    if new_rock_pos_right not in rocks:
        # falling down and to the right
        return new_rock_pos_right, True
    # not falling
    return new_rock_pos, False


def print_rocks(rocks):
    rock_arr = []
    for i in range(494, 504):
        row = []
        for j in range(0, 10):
            row.append(".")
        rock_arr.append(row)

    for r in rocks:
        rock_arr[r[1]][r[0]-494] = "#"

    for r in rock_arr:
        print("".join(r))


if __name__ == "__main__":
    main(argv[1])
