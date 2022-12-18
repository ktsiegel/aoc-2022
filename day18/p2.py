from sys import argv


def main(filename):
    # Read the input file
    with open(filename, "r") as f:
        input = [[int(y) for y in x.strip().split(",")] for x in f.readlines()]

    total_sides = len(input) * 6

    rocks = set()
    for l in input:
        rocks.add((l[0], l[1], l[2]))

    min_i = 10000000000
    max_i = -1
    min_j = 10000000000
    max_j = -1
    min_k = 10000000000
    max_k = -1
    for l in input:
        (i, j, k) = l
        min_i = min(min_i, i)
        max_i = max(max_i, i)
        min_j = min(min_j, j)
        max_j = max(max_j, j)
        min_k = min(min_k, k)
        max_k = max(max_k, k)
        poss = [(i+1, j, k), (i-1, j, k), (i, j+1, k),
                (i, j-1, k), (i, j, k+1), (i, j, k-1)]
        for p in poss:
            if p in rocks:
                total_sides -= 1

    searched = set()
    q = [(min_i-1, min_j-1, min_k-1)]
    air_sides = 0
    while len(q) > 0:
        curr = q.pop(0)
        if curr in searched:
            continue
        searched.add(curr)
        (i, j, k) = curr
        adj = [(i+1, j, k), (i-1, j, k), (i, j+1, k),
               (i, j-1, k), (i, j, k+1), (i, j, k-1)]

        for p in adj:
            if p not in searched:
                (pi, pj, pk) = p
                if pi >= min_i-1 and pi <= max_i+1 and pj >= min_j-1 and pj <= max_j+1 and pk >= min_k-1 and pk <= max_k+1:
                    # find number of adjacent cubes
                    if p in rocks:
                        air_sides += 1
                    else:
                        q.append(p)
    print(air_sides)


if __name__ == "__main__":
    main(argv[1])
