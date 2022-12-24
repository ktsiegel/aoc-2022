from sys import argv
from math import ceil


class Factory:
    def __init__(self, blueprint):
        tokens = blueprint.split(" ")
        self.ore_cost = (int(tokens[6]), 0, 0, 0)
        self.clay_cost = (int(tokens[12]), 0, 0, 0)
        self.obsidian_cost = (int(tokens[18]), int(tokens[21]), 0, 0)
        self.geode_cost = (int(tokens[27]), 0, int(tokens[30]), 0)

    def __str__(self):
        return f"ore: {self.ore_cost} ore, clay: {self.clay_cost} ore, obsidian: {self.obsidian_cost[0]} ore {self.obsidian_cost[1]} clay, geode: {self.geode_cost[0]} ore {self.geode_cost[1]} obsidian"

def get_ts_after_build(costs, ts, robots, resources):
    min_ts = 0
    for i in range(len(costs)):
        if resources[i] < costs[i] and robots[i] > 0:
            min_ts = max(min_ts, ceil((costs[i] - resources[i]) * 1.0 / robots[i]))
    return min_ts+1

def sub_resources(resources, costs):
    return tuple([resources[i] - costs[i] for i in range(len(resources))])

def add_resources(resources, robots, ts):
    return tuple([resources[i] + robots[i] * ts for i in range(len(resources))])

max_t = 32
def main(filename):
    # Read the input file
    with open(filename, "r") as f:
        factories = [Factory(x.strip()) for x in f.readlines()][0:3]

    score = 1

    for fi in range(len(factories)):
        f = factories[fi]
        # (ts, robots, resources) -- ore, clay, obsidian, geode
        q = [(0, (1, 0, 0, 0), (0, 0, 0, 0), "")]

        max_geodes = 0
        seen = set()

        while len(q) > 0:
            curr = q.pop(-1)
            (ts, robots, resources, log) = curr 
            (ore_robots, clay_robots, obsidian_robots, geode_robots) = robots
            (ore, clay, obsidian, geode) = resources

            memo = (ts,) + robots + resources
            if memo in seen:
                continue
            seen.add(memo)

            geodes_at_end = geode + (geode_robots * (max_t-ts))

            max_geodes = max(geodes_at_end, max_geodes)
            max_potential_geodes = (max_t - ts - 1) * (max_t - ts) // 2
            if max_geodes > geodes_at_end + max_potential_geodes:
                continue

            # decide which robot to build next
            ore_ts = get_ts_after_build(f.ore_cost, ts, robots, resources)
            if ore_ts + ts <= max_t:
                q.append((ts+ore_ts, (ore_robots+1, clay_robots, obsidian_robots, geode_robots), sub_resources(add_resources(resources, robots, ore_ts), f.ore_cost), log + f"ore ({ore_ts+ts}) "))

            clay_ts = get_ts_after_build(f.clay_cost, ts, robots, resources)
            if clay_ts + ts <= max_t:
                q.append((ts+clay_ts, (ore_robots, clay_robots+1, obsidian_robots, geode_robots), sub_resources(add_resources(resources, robots, clay_ts), f.clay_cost), log + f"clay ({clay_ts+ts}) "))

            if clay_robots > 0:
                obsidian_ts = get_ts_after_build(f.obsidian_cost, ts, robots, resources)
                if obsidian_ts + ts <= max_t:
                    q.append((ts+obsidian_ts, (ore_robots, clay_robots, obsidian_robots+1, geode_robots), sub_resources(add_resources(resources, robots, obsidian_ts), f.obsidian_cost), log + f"obsidian ({obsidian_ts+ts}) "))

            if obsidian_robots > 0:
                geode_ts = get_ts_after_build(f.geode_cost, ts, robots, resources)
                if geode_ts + ts <= max_t:
                    q.append((ts+geode_ts, (ore_robots, clay_robots, obsidian_robots, geode_robots+1), sub_resources(add_resources(resources, robots, geode_ts), f.geode_cost), log + f"geode ({geode_ts+ts}) "))

        print("max", max_geodes)
        score *= max_geodes 
        print(score)

    print(score)


if __name__ == "__main__":
    main(argv[1])
