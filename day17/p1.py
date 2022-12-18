from sys import argv


def rock0(max_y):
    y = max_y+3
    return [(2, y), (3, y), (4, y), (5, y)]


def rock1(max_y):
    return [(3, max_y+5), (2, max_y+4), (3, max_y+4), (4, max_y+4), (3, max_y+3)]


def rock2(max_y):
    return [(4, max_y+5), (4, max_y+4), (2, max_y+3), (3, max_y+3), (4, max_y+3)]


def rock3(max_y):
    return [(2, max_y+6), (2, max_y+5), (2, max_y+4), (2, max_y+3)]


def rock4(max_y):
    return [(2, max_y+4), (3, max_y+4), (2, max_y+3), (3, max_y+3)]


def print_rocks(rocks, max_y):
    y = max_y
    while y >= 0:
        line = ""
        for x in range(7):
            if (x, y) in rocks:
                line += "#"
            else:
                line += "."
        print(line)
        y -= 1
    print("\n")


def main():
    jet = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"

    # jet = "><<<<><<>><<>><><<<>>><<<<>>>><<>>><>>><<<>><<<><<<><><><>>>><<>>><<<<>>><>><<<<>><><<<<>>><<<>>><<>><<<>>><>>>><<<<>>>><<<<><>><<<>>><<<<>><<<<>>>><<<<>>><<>>><<<>>><>>><<<<>>><<<<>>>><>>>><<>>><<><<<>>>><><<<<>>>><>><<>><<<><<<<>><<><<<<>>><>><<><<<>>><<<>>><<><<<<>><>><<<><<<>>>><>>>><<<>><<<<>>>><<<>>>><><<<<>>>><<<<>>>><<<<><<<>>>><><<<>>><<<><<><<<>>><<<><<>>>><<<>>>><<<>>><<><>>><<><>>>><><><<>>><<<>><<<>><><>>><<<>>><<<<><>><>>>><<><<<>>>><<><<<<>>><><<>>>><<<<>>>><<><<<<>><<><><>>>><<>><<>><<<<><>>><><<<>><<<>><><>>>><<<>><<<<>>><<><>>>><>>>><<<>>><<<<>>><><<<<>>><>>>><>>><<>>>><<>><<>>><<>><><>><<<<>>><<><<>><<<<><<<>>>><>>><>>><<<>>><<<>>>><<>>><<<<>><<>>>><><<<><>><<<><<<<>>><><<<><<<<>><>><<<<><<<>><>>><<<<>>>><<>>>><<<<>>><><<<>>><<<<><>><<<>><<<<><>>><>>>><<>>><<<>>>><<>>><><<<><<<<><<><>>>><><>>>><<>>><<<<>><<<<><<>>><<><<<><<<<>>><><<<>>>><>>>><<<><<<>><<><<<>>>><<<<>><><<<<>>>><<>>>><<>><<>><<<>><<<<>><>>><<<<>>>><><<>>><<>>><>>><<<<>>><<<<>>><<>><>><<<>><<<>>>><<<>>>><<>><<<><><>>><<<<>><<>>>><<><><<<><>>>><<<>><<<>>>><<<<><<>>><<>>>><<><<<<>><<>>><<<<>><>>><<>>>><<<<><><>>><<<<>>>><>>>><<>>>><<<<><<>><<<><<<>><<<>>>><<<><<<<>><<<<>><<<<>>>><<<>>>><>><<<>>>><<<>>><<><><<<>><<<>><>>><>><><<<<>><<<<>>>><<<>>><>>><<><><<>>>><<<<><><<<>>>><<>><<>>><<<<>>>><>>>><>><<<>><<<<>>>><><<><<>>>><<<>><<>>><<<<>><<>>><<<<>>>><<<>>><<<><>><<><>>>><<>>>><<<><>>><>>>><<<<>>><<<>><<>>><<<<><<<>>><<>>><<<<>>><<>><<<><>>><><>>>><<>>>><<>><<<<><<<>>><<<<>><<<>><>><<<>><>>><<<>>>><>><><<>>><<>>><<<>>><<>><<<<>>>><<>><<>>><<>>><<>>><<>><><<<>>>><>>>><><<<>>><>>><<<<>>><<<<><>>>><<<<><<><<<>>>><<<>><<<><><<<<>>><<>>><<<<>>>><<>>><<<><<<<>>>><<<<>><<<><<>>><>><<>><<<<>><>>>><<>><<<>>><<<><<>>><<<><<<<><<<<><<>><>>>><>><>><<>>><<<<>>>><<<<>>><<<<><<<<><<<><>>><>>><<<<>><<>>>><><>>><>>>><><>>>><<<>><<>><<<<><>>>><<<><<<<><>>>><<>>><<<>>>><<>>>><<<<><<<<>>>><<><<<<>><<<>><>>><<<<><<>><<<>>><>><<<<>>>><<>>><<<>>><>><<<>>>><>><<<><<<<>>><<<<>><<>>><<<>>>><<<>>><><<><<<><<>>>><<>>><<>>>><>>>><<<<><><>>>><<<>>><<<>>>><<>><<<<><<<>>><<<>>>><>><<>>><<<>>>><>><><<<<>>>><>><<<<>>>><<<<>><>>>><<><<<<>><><<<>>><<<<><<<<><>><>>>><<<>>>><<<>><<>>>><>><<<>>><<<>>><<<<>>><<<<><<>><<<<>><>>><>>><<>>><<<><<<<>>>><<<>>><<>>><<<<>><><<<>>>><><<<<>>><<<>>><<<>><<>>>><<>>><<<<>>><<>>><>>>><<>><<<>>>><<<<>>>><<<<><<><><<>>>><<<<><<>>><<<<>>><<<<>><<><>>><>><<>>>><<<<>><<<>>><<<<>><<>><<><<>>><<<>><<<>>>><<>>><<<>>>><<<<>>><<<<>><<>>>><<<>>>><>><<<<>>><>>><<><<>>>><<<>>><>>><<<>><<<<><><<<>>><<<><<<>><<<<><<<>><<<<>>>><>><>><>>>><<<><<<>>><<<><<<<>>>><<>>>><<<>><<>><<<<>><>><<<><<<<>><<<>>>><<>>>><<>>>><>>>><<<<>>><<>>>><<>>>><<>><<<>>><>>>><<<<><>>>><<<<><>>>><<<>>>><<<<>>><<<<>><><<<<>>><><>><<<<>>><<<>>><><<<>>>><<<>>>><<><<<<><<<<><<><<<<>>><>>>><<>>>><<<>>>><<<>>><<<<>>><>><<<><<<<>>>><<<<>>><<<<>>>><<<<><<<>><<<>>>><<<><<<<><>><<<<>><><<<>>><>><<<>>><<>><<>>><>><>>><<>>><<<>>>><>><<<>><<>>><<<<>>>><>><><<>><>><<<<><><<>>><<<<>>>><<>>><<<<>>><<<<><>>><<<>>>><<<<>>><<<>>>><<<>><<><><<<<>>><<>>>><<>>><<><<<<>>>><>><<>><<<<>><>>><<<<>><<>>>><<<<>>><<>><>><>><><<<>>>><<<>>><<>><><<>>>><<<>>><<<>>>><<<<><<<>><>>><>>>><<<<><<<<>>>><<<>><<<<><<<<>>><<<<>>>><>>><<<<>>>><<<>><<<>><<<>>><<<<>>><<<>>>><>>><><<>>><>>>><<>>><<>>>><<<>><<<><<>>><<>>>><<<<>><><<<<><<<>><>>>><<<<>>>><<<<>>><<<<><><>>>><<>><>>><<>>>><<>>>><<<<>>><><<>>><<<<><<<><<>>><>>><>><>>>><>><<<>>>><<>>><<<>>><<>><<<<>>><<>>><<><<<<><<>>>><<<<><>>>><<<>><<><<<<><<><<>>>><<><<<<>>><<>>><>><>>><>>>><>>>><<>><<<<><<<<>>>><>>><<>>>><<<<>>><<><<<<>>><<<<>><>>>><>><<<<>>><<>><<<>><<>>><<<<>>>><<<>>>><>>>><>>>><<<<><>>><>>>><<<>><>><<><<<><<>>>><<<<>><<>>><<>>><<<<>><<<<><<<>>>><<<>><<>>>><<<>>>><<><><<<<>>>><><<>>><<>>>><<<>>><<>><<><<<><<<>>>><><<<>>><<<<>><>>>><<<><<><<<<>>>><<><<<<>>>><<<>><><<>>>><>>>><<<<><<<><<<>>>><<>><>>><<<>>>><<>>>><>><<<><<><<<<>>>><<>>>><<<>><<>><<<<><<>><<<>>>><<><<<>>><<<<>>><<<<><<>><<<>>>><>>>><<<<>>><>><<<<>>>><<<><<<<>>>><<<>>>><<><<<<>>>><<<<><<>>>><<><<><>>><>>><>>><>>>><<<<><<<<>>>><>><<<<>><<<<>>><<<<>>>><>><<<>>>><>>>><>>>><<>>>><>><<<>><><<>><<>>><>><><>>>><>>>><>>>><<<>><<><<<<>>>><><>>><><>><>><<>>><<>><<>>><<<<><<<>>><<<<>>>><<<<><<<>>><<<<>>>><<<<>>>><>>><><>><<<<>>>><<<<>><<><><<<><<>><<<<>><<<>><<<>>><<<>><<<>><><<>>>><<<<><<>>>><<><<<>><<<<>>><<<>>><<<>><>><<<<>><<<<><<<<>><<<<><>>><<<<>><<<<>>><<<<><<><>><<<>><>>>><>>>><>>>><<<<>><<<<><<>>><>>>><<<<>>><<<><<<>>><<<>><<><<>>><<<>>>><<<>>>><<<<>><>>>><<<<>>><>>><<>>>><<>>>><>>><<<><>>><<<><>>>><<<<>>><<<>><<<>>>><<<<>>>><<><><><<<><<>>>><<<<><<<>><<>><<<<>>><<>>><<<><<<>>>><<>><>>><>>><<<<><<<>>><<<><<<><<<>><<>>><<><<>>>><<<<>>><<<>>>><<>><<<<>>>><<><<<<><<>>><<<><>>>><<<><<>>>><>>><<>>><<<<>><<>>>><<<>>><<<>>>><<<<>>>><<<><<<>>><<<><<<>>><<<<><<>>>><>>>><<<>>>><>>><>>>><<<>><<<<><<<<><<<<>><<<<><<<<><>><<><<<<>>><<<<>>><<>>><<<>>>><<<>>>><<<>><<<>><<<><<<>>><<>>>><><<<>><<<>>><<>><<<<><<>>><>><<<>>>><<<<>>>><<>>><<>><<><<<<><<<>>>><<<<>>>><<>>><<>><<<>>><>>>><<<>><>>>><<>>>><<<<>><<<<>>>><<>><>>><><<><<>>>><<>><<><>>>><<>><<<<>>>><>>><><<<<>>><<<<>>>><<>>>><<>>>><<<<>><<<>>><<>>><>>>><<<><<<><<<>><>><><>>>><<>><<<<>><<<<>><><>><<>>>><<<><<<><>>><<<>>><<<>>>><<<>>><<<>>>><>>>><<<>><>>>><<<>>>><<<>>>><<<<><>>>><<<<>>>><>>><<<>>><<>><<><<<>>>><<<>>>><<<>><>><<<<>><<<>><<<>>><<<<><<<<>>>><<<<>>><<<<>><<<<>><<><>>><<<>>><<<<><<<>>><<<<><>>><<<>>>><>>>><><<<<>>>><><>><<>>>><>>><<<<>>><<<>><>><<<<><<<<>>><><<<<>>>><>><>><<<<>><<>><<<<>><<>>><<>>><<<>>>><<>>><<>><<<<>>><<>>>><<><<>><<<<>>><<<<><<<<><<<><>>><<>><<<<><<<>>>><>>>><><<<><<><<<<>><<<>><>>>><<<<>><<><<<><<<<>>>><<<><<>>>><><<><<<<><<<<>>><<<<>>>><<>>><<<><<<>>>><><<>>>><><<><<<<><<>>>><><<>><<>><>>><<><<<>><<>>>><<<<><<<<><><>>>><<<<>>><<<<>>><<>>>><<<><<<>><<<>>>><<<<><<<<>><<<<>>><<<<>>><>>><<<><<><<<<>>>><>><<>>><>><<<<>>><>>>><<>>>><<<<><<>>><<<<><<>><><<>>>><>><<>><<<<>><<>><<<<><<<<>>>><<<>><<>>><<><<<<>>>><<<>>>><<>>>><>>><<<>>><><<>><<>>><>>><>>>><<>>><<<>>>><><<<<><<>><<<<>>>><>><<<<><<<<><<<<>>>><<<><<<<>><<<>>>><<<<>><>>>><>><<<<>><>>><><<<>><><<<<>>><>>><<<>>>><<<>><<<<><<><<<><>>><>>>><<>>>><<<<>>><>>>><>>>><<>><<>>><<<<>>><<>>><<>>>><<<><<>>>><<<<>><>><<<>>><<<<>>>><>>><<<>>>><<<>><<>><<>>>><<<>>><<<>>>><>><<>><<<<><>>>><>><<>><>><>><>><<<>><<><>>>><>>><<<<>>><<<>><<<<>><<<<>><><<<<><<<<>><<<<>>><<>>>><><<<<>><<<<>><<<<>><>><>>><<><<>>><<<><<<>>><>>><><<<>>>><<<<><<<>>>><<>><>>><<><<>><<<>><<<<><<<<>>><>>><<><<>>>><<<><<><<<<>>>><<<<><<>><>>><<<<><<<>>>><<>><<<><<<>>><>>>><>>><<>>><>>><<<<>><>>>><<><>>>><<<><<><<<<>>><<<>>>><<><><<>><<<<><<>><<><<<<>><<><<><<<<>><>><<<>>><<><<<>>><<<<>>><>>><><><<>>>><<><<<<><>><>>>><<<<><<<<>>><<<<>>>><>><<<>><<<>><<<<>>><<>>><<<<>>>><<<<>><<>><<>><<<<>><>>>><<><>>>><<<>>>><<<>><>>>><<<>>><<>>><<>><><<<<>>><<>><<<<>><<<><<>>><<<>>>><<>>><<>>>><<<<>>>><>>><><<<<>>><<<>>><<<>><<>>><<<<><<<>><<<>><<><>>><<<<><<>><<<<>><<><<><>>>><>>><<>>>><<<<>>><<><<<>><<<>>>><<>>>><>>>><<>><<<>>><>>>><<>><<<>>>><<<>><<<<>>>><<<<><<>>><>>><<<><<>><>>><>>><<<>><<<<>><<<>>><>><<<>><<<<>>><<><><<<<>><<<><<<<>>><>>>><<<><<<<>><<<>><<><<<>>>><<<<>><>>><<<>><<>>><<<>><<<>>>><<<>>><<<<><<>><><<<>>><<<<>>>><<>>><>>>><<>>><<<<>>><>><<<>><>><<<<>><<<<><<>>><<><<>>>><<<><>>>><<<>>><<<>>><<>><<<<>>><<>>>><<<<>>><<><<<>><<>>>><<<<><<<<>>>><<<<>>><<<>><<>>><<<><>>><<>>><><>>>><<>><>><<<<>>>><<<>>><<<<>>>><>><<<<>><<>><<<>>><<<<>>><<<>>><<>><<<>>>><<>>><<>><<<><<<>>><<>>><<<>>>><<<<>><<<<>><<<>>><<<>>><<>>>><<<<>>>><<><<<<><>><>>>><<><<>>><<<<><<<<>>>><>>><<<><>><<>>><<<<>>><<>>>><<<>>>><>>>><<<>><><<>>><<><<<>><<>><>>><<<<>><>>>><<>><>>><<<<>><<>>>><<><<<<>>>><<<>>><>>><<<><>>><>><<<<><>>>><<<<><<<<>>><>>><><<>>><<>>><><<<<><<<><>><>>>><<<>>>><><>><><>><<<<><<<><<<>>>><<<>>><<>>><<<>><<<><<>>><>>>><<><<>>>><<<<>><<>><>>><<<<>>><<<>>>><<<<>><<<<>>>><<>><<<>><<<>><<<>>>><<<<>>>><>><<<<>>>><><><>>><>>><<<>>><>><<<<>>>><<><<<>>>><<>>><<<><<<<>><<<><>>><<>>><<<<>>>><><<<<>><<<>><<<>><<<>><<>>>><<<>>>><<<>>><<<><<<><<<><<<<><>><<>>><><<<><<<>>><<<<>>>><<<>>><>>><><<<>><<<>>>><<><><<<<>>>><<><<<>>>><<<>>>><<><<<<>>>><<<><<<>>>><<>>>><<><><<<<>>><<<><<<><><<>>>><<>>>><<<>>>><<>><<><>>>><<<<>>>><<<<>>><<<<>><<<><<><>><<<>>>><>><>><<<<><><><><<<<>>><<<<>><<>><>><<>><<<>>>><<<>>>><<<<>>>><<<>><<<>>>><<>>>><<<><<<>>><>>><<<>>><<<<>>><<<<>>><>>><<<<>>><<<<>>><<<>><<<<><<<>>><<<<>><<<><<<>>><<<<>><<>><<<<><<<<><><>>><<>><><<<<>>>><<>>><<<>><<><><>>><>>>><>>>><<<<>>><<<<>>>><<>>><<<<><<<<>>>><<>><<<>>><<>>>><<<>><<<<>><><<<<>>><<>><<<<>>><<<<>>><>>><>>><<<<>>><<<<>>>><>>>><<<<>>><><<><>>>><><<<<>>><>>>><<>>>><<><<<<>>><<<>>>><<<>>><<<<>><<<><<<<><<<<>><<<>>>><<<<>>><<<><<<<>>><<<<>>><<>>><<<>>>><>>>><<>>><<<><<<><<<<>><<<<>>>><<>>><<<>>>><<<>><<<<><<<>>>><<<<>><<<<><<><<<<>>><<<>>>><<<><>><<<>><>><<>>><<><<<><><<<>><<>>>><<><>><<<>>><<>>>><>>>><<<<>>><<>>>><<>>><<>><<<><<<<><>>><<><<><>>><<<<>>>><<<>>>><<>>>><<<<>>>><<<><<<<><>>><<>><<<><<>>><>>><<<>>><<>>><<>>>><<><<<<>>><>><>><<<><<<<>><<<<>>>><>>><<>>>><<<<>><<>>>><<><>><<<>><<<><<<>>>><<>><<<>>><<<<>>><>>><>>><<<<>>>><<<>><<<>><<<<><<<>><<<>>><<>><<<>><<>><<<>>><<<<><<>>>><<><>><<>>><<<>>>><><>>>><>>>><><<<<>>>><<>><<>><>>>><<>><<>><<<<>><<>><<<<>>>><>><<<<><><>><<>><<<<>>><<<<>><<<><<<>><<<><<<>><<<<>>>><>>><<<>>>><<<>>>><<<>>>><<>>>><<>><>>>><<<>>><<<<>><>>><<<>><>>><<<>>>><<<<><>><<<<><<>>>><<<>>>><<<<>>><>>><<<<><<>><>>><<<>>><>>>><<<>>><<<>><><>><<>>><<<>><<<>><>><<>>><<<>>><><>>><<<>>>><<><>>><<>>>><<<<>>>><<<<>><<<<><<>>>><<<>><<>>>><<>>><<>>><<>>><<><<<<><<<>>><<<><>>><<<<><<<>>>><<<>>>><<<<><<>>>><<<>><<<>>>><<<<>>>><<<<>>><>>><<><<<><<<>>><<<<>>>><<<<>>>><<><><<<<>>>><<>><<<<>>><<<>><>>><<<>>><>><<<>>><>><<<><<>><>>><<<>><<>><>><<>>><>><<<><<<>>><<<<>><<<<>>><>>>><<<<><<<<>>>><>>><><<<<>>><<<<>>>><>><<>>>><<<<>>><<<<>><><<>>>><<>>><<<<>><<<>>><<<><<<<>>>><>><<>>><<>>><>>><<>>><<>><<<<>><<>>>><<<<>><<>>><<>><<>>><>>><<<>>>><<<>>>><<<<>>><>><<<>>><<<><<>>>><><<<>>>><<>><<>>>><>>><<>>>><><<>>><<<><>><<<>><>>>><>>>><<<>><<>>>><>><<>>>><<>><<<<>>>><<<<><>>><>>>><<>><<><<<><<><<<<>>><<<<>>>><<>><<>>><><<<>><>>>><<<>>><><<><<<>>><<<<>>><>>><<><<><<>><>><<><<>>><<<<"

    t = 0
    rocks = set()
    rock_max_y = 0
    gas_idx = 0

    while t < 2022:
        # breakpoint()
        new_rock_num = t % 5
        if new_rock_num == 0:
            new_rock = rock0(rock_max_y)
        elif new_rock_num == 1:
            new_rock = rock1(rock_max_y)
        elif new_rock_num == 2:
            new_rock = rock2(rock_max_y)
        elif new_rock_num == 3:
            new_rock = rock3(rock_max_y)
        else:
            new_rock = rock4(rock_max_y)

        while True:
            # print_rocks(rocks.union(set(new_rock)), rock_max_y+6)
            # first pushed by jet of gas
            gas_dir = jet[gas_idx]
            if gas_dir == ">":
                can_move = True
                moved_rock = []
                for sub_rock in new_rock:
                    if sub_rock[0] >= 6 or (sub_rock[0]+1, sub_rock[1]) in rocks:
                        can_move = False
                        break
                    moved_rock.append((sub_rock[0]+1, sub_rock[1]))
                if can_move:
                    new_rock = moved_rock
            elif gas_dir == "<":
                can_move = True
                moved_rock = []
                for sub_rock in new_rock:
                    if sub_rock[0] <= 0 or (sub_rock[0]-1, sub_rock[1]) in rocks:
                        can_move = False
                        break
                    moved_rock.append((sub_rock[0]-1, sub_rock[1]))
                if can_move:
                    new_rock = moved_rock

            gas_idx += 1
            gas_idx = gas_idx % len(jet)

            # print_rocks(rocks.union(set(new_rock)), rock_max_y+6)

            # then move down
            can_move = True
            moved_rock = []
            for sub_rock in new_rock:
                if sub_rock[1] <= 0 or (sub_rock[0], sub_rock[1]-1) in rocks:
                    can_move = False
                    break
                moved_rock.append((sub_rock[0], sub_rock[1]-1))
            if can_move:
                new_rock = moved_rock
            else:
                break

        # update rock max y
        for sub_rock in new_rock:
            rock_max_y = max(rock_max_y, sub_rock[1]+1)
            rocks.add(sub_rock)

        t += 1

    # print_rocks(rocks, rock_max_y)
    print(rock_max_y)


if __name__ == "__main__":
    main()