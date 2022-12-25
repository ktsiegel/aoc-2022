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
    q = [(("AA", "AA"), 26, 0, set(), (set(["AA"]), set(["AA"])))]
    memo = dict()

    max_pressure = 0
    max_valves_open = [0]*27
    while len(q) > 0:
        curr = q.pop(-1)
        max_pressure = max(curr[2], max_pressure)
        tleft = curr[1]

        me_and_el = tuple(sorted([curr[0][0], curr[0][1]]))
        memoized_open = me_and_el + (tleft, len(curr[3]))
        if len(memoized_open) > 0 and memoized_open in memo and memo[memoized_open] >= curr[2]:
            continue
        memo[memoized_open] = curr[2]

        max_valves_open[tleft] = max(max_valves_open[tleft], len(curr[3]))
        if max_valves_open[tleft] > len(curr[3]) + tleft: # can maximally open up tleft valves
            continue

        # four options:
        # both open
        # I open, elephant moves
        # elephant opens, I move
        # neither open, both move
        next_time = curr[1]-1
        me = curr[0][0]
        elephant = curr[0][1]
        flow_rate_me = maze[me][0]
        flow_rate_elephant = maze[elephant][0]

        # neither open, both move
        for d_me in maze[me][1]:
            if d_me not in curr[4][0]:
                for d_elephant in maze[elephant][1]:
                    if d_elephant not in curr[4][1]:
                        q.append(((d_me, d_elephant), next_time, curr[2], curr[3], (curr[4][0].union(set([d_me])), curr[4][1].union(set([d_elephant])))))

        if flow_rate_me > 0 and me not in curr[3]:
            # I open, elephant moves
            next_pressure = curr[2] + (next_time * flow_rate_me)

            # elephant moves to any of the destination rooms
            for d in maze[elephant][1]:
                if d not in curr[4][1]:
                    q.append(((me, d), next_time, next_pressure,
                            curr[3].union(set([me])), (set(), curr[4][1].union(set([d])))))
        
        if flow_rate_elephant > 0 and elephant not in curr[3]:
            # elephant opens, I move
            next_pressure = curr[2] + (next_time * flow_rate_elephant)

            # I move to any of the destination rooms
            for d in maze[me][1]:
                if d not in curr[4][0]:
                    q.append(((d, elephant), next_time, next_pressure,
                            curr[3].union(set([elephant])), (curr[4][0].union(set([d])), set())))

        # open valve is only an option if the flow > 0 and the valve is not already open
        if flow_rate_me > 0 and me not in curr[3] and flow_rate_elephant > 0 and elephant not in curr[3] and me != elephant:
            # both open
            next_pressure = curr[2] + (next_time * flow_rate_me) + (next_time * flow_rate_elephant)
            q.append(
                ((me, elephant), next_time, next_pressure, curr[3].union(set([me, elephant])), (set(), set())))

       

    print(max_pressure)


if __name__ == "__main__":
    main(argv[1])
