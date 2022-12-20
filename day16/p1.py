from sys import argv


def main(filename):
    # Read the input file
    with open(filename, "r") as f:
        input = [x.strip().split(" ") for x in f.readlines()]

    maze = dict()
    for l in input:
        curr = l[1]
        dests = [x.strip().replace(",", "") for x in l[9:]]
        flow_rate = int(l[4].replace("rate=", "").replace(";", "").strip())
        # flow rate, destinations, max_pressure_released at each time
        maze[curr] = [flow_rate, dests]

    # (node, time left, pressure released, open_valves, visited)
    q = [("AA", 30, 0, set(), set(["AA"]))]
    memo = dict()

    max_pressure = 0
    while len(q) > 0:
        curr = q.pop(0)
        max_pressure = max(curr[2], max_pressure)

        # memoized_open = tuple([curr[0]] + sorted(list(curr[3])))
        # memoized_open = (curr[0], curr[1], len(curr[3]))
        memoized_open = (curr[0], curr[1], len(curr[3]))
        if len(memoized_open) > 0 and memoized_open in memo and memo[memoized_open] >= curr[2]:
            continue
        memo[memoized_open] = curr[2]

        # two options: open valve or move to next room
        next_time = curr[1]-1
        flow_rate = maze[curr[0]][0]

        # open valve is only an option if the flow > 0 and the valve is not already open
        if flow_rate > 0 and curr[0] not in curr[3]:
            next_pressure = curr[2] + (next_time * flow_rate)
            q.append(
                (curr[0], next_time, next_pressure, curr[3].union(set([curr[0]])), set()))

        # we can also move to any of the destination rooms
        for d in maze[curr[0]][1]:
            if d not in curr[4]:
                q.append((d, next_time, curr[2],
                         curr[3], curr[4].union(set([d]))))

    print(max_pressure)


if __name__ == "__main__":
    main(argv[1])
