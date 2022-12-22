from sys import argv
from enum import Enum
from math import ceil


class RobotType(Enum):
    ORE = 1
    CLAY = 2
    OBSIDIAN = 3
    GEODE = 4


class Factory:
    def __init__(self, blueprint):
        tokens = blueprint.split(" ")
        self.ore_cost = int(tokens[6])
        self.clay_cost = int(tokens[12])
        self.obsidian_cost = (int(tokens[18]), int(tokens[21]))  # ore, clay
        self.geode_cost = (int(tokens[27]), int(tokens[30]))  # ore, obsidian

    def __str__(self):
        return f"ore: {self.ore_cost} ore, clay: {self.clay_cost} ore, obsidian: {self.obsidian_cost[0]} ore {self.obsidian_cost[1]} clay, geode: {self.geode_cost[0]} ore {self.geode_cost[1]} obsidian"


def main2(filename):
    # Read the input file
    with open(filename, "r") as f:
        factories = [Factory(x.strip()) for x in f.readlines()]

    score = 0

    for fi in range(len(factories)):
        f = factories[fi]
        # (ts, robots, resources) -- ore, clay, obsidian, geode
        q = [(0, [1, 0, 0, 0], [0, 0, 0, 0], "")]

        geode_memos = [0]*24

        max_geodes = 0
        while len(q) > 0:
            (ts, [ore_robots, clay_robots, obsidian_robots, geode_robots],
             [ore, clay, obsidian, geode], log) = q.pop(-1)

            if ts == 24:
                if geode > max_geodes:
                    print(f"ts: {ts}, ore: {ore}, clay: {clay}, obsidian: {obsidian}, geode: {geode}, ore_robots: {ore_robots}, clay_robots: {clay_robots}, obsidian_robots: {obsidian_robots}, geode_robots: {geode_robots}, log: {log}")
                max_geodes = max(max_geodes, geode)
                continue

            if geode >= geode_memos[ts]:
                geode_memos[ts] = geode
            elif geode_memos[ts] > 0:
                continue


            # decide which robot to build next
            
            # build an ore robot next -- requires at least one ore robot
            diff_ore = max(f.ore_cost-ore, 0)
            diff_ts = ceil(diff_ore * 1.0/ore_robots)+1
            if ts + diff_ts <= 24:
                new_resources_ore = [ore + (ore_robots*diff_ts) - f.ore_cost, clay+(clay_robots*diff_ts), obsidian+(obsidian_robots*diff_ts), geode+(geode_robots*diff_ts)]
                nlog = log + f" ore ({ts+diff_ts}) "
                q.append((ts+diff_ts, [ore_robots+1, clay_robots, obsidian_robots, geode_robots], new_resources_ore, nlog))

            # build a clay robot next -- requires at least one ore robot
            diff_ore = max(f.clay_cost-ore, 0)
            diff_ts = ceil(diff_ore * 1.0/ore_robots)+1
            if ts + diff_ts <= 24:
                new_resources_clay = [ore + (ore_robots*diff_ts)-f.clay_cost , clay+(clay_robots*diff_ts), obsidian+(obsidian_robots*diff_ts), geode+(geode_robots*diff_ts)]
                nlog = log + f" clay ({ts + diff_ts}) "
                q.append((ts+diff_ts, [ore_robots, clay_robots+1, obsidian_robots, geode_robots], new_resources_clay, nlog))

            # build an obsidian robot next -- requires at least one ore robot and one clay robot
            if clay_robots > 0:
                diff_ore = max(f.obsidian_cost[0]-ore,0)
                diff_clay = max(f.obsidian_cost[1]-clay, 0)
                diff_ts_ore = ceil(diff_ore * 1.0 / ore_robots)
                diff_ts_clay = ceil(diff_clay * 1.0 / clay_robots)
                diff_ts = max(diff_ts_clay, diff_ts_ore)+1
                if ts + diff_ts <= 24:
                    nlog = log + f" obsidian ({ts + diff_ts}) "
                    new_resources_obsidian = [ore + (ore_robots*diff_ts)-f.obsidian_cost[0], clay+(clay_robots*diff_ts)-f.obsidian_cost_ore_clay[1], obsidian+(obsidian_robots*diff_ts), geode+(geode_robots*diff_ts)]
                    q.append((ts+diff_ts, [ore_robots, clay_robots, obsidian_robots+1, geode_robots], new_resources_obsidian, nlog))

            # build a geode robot next -- requires at least one ore robot and one obsidian robot
            if obsidian_robots > 0:
                diff_ore = max(f.geode_cost[0]-ore,0)
                diff_obsidian = max(f.geode_cost[1]-obsidian, 0)
                diff_ts_ore = ceil(diff_ore * 1.0 / ore_robots)
                diff_ts_obsidian = ceil(diff_obsidian * 1.0 / obsidian_robots)
                diff_ts = max(diff_ts_obsidian, diff_ts_ore)+1
                if ts + diff_ts <= 24:
                    nlog = log + f" geode ({ts + diff_ts})"
                    new_resources_geode = [ore + (ore_robots*diff_ts)-f.geode_cost_ore_obsidian[0], clay+(clay_robots*diff_ts), obsidian+(obsidian_robots*diff_ts)-f.geode_cost_ore_obsidian[1], geode+(geode_robots*diff_ts)]
                    q.append((ts+diff_ts, [ore_robots, clay_robots, obsidian_robots, geode_robots+1], new_resources_geode, nlog))

            # or, just fast forward to the end and build no robots
            diff_ts = 24-ts
            new_resources = [ore + (ore_robots*diff_ts), clay+(clay_robots*diff_ts), obsidian+(obsidian_robots*diff_ts), geode+(geode_robots*diff_ts)]
            q.append((24, [ore_robots, clay_robots, obsidian_robots, geode_robots], new_resources, log))



        print("max", max_geodes)
        score += ((fi+1)*max_geodes)
        print(score)

    print(score)

def main(filename):
    # Read the input file
    with open(filename, "r") as f:
        factories = [Factory(x.strip()) for x in f.readlines()]

    score = 0

    geode_memos = [0]*24

    for fi in range(len(factories)):
        f = factories[fi]
        seen = set()
        # (robots, resources) -- ore, clay, obsidian, geode
        q = [(0, 1, 0, 0, 0, 0, 0, 0, 0)]

        highest_ore_cost = max(f.ore_cost, f.clay_cost,
                               f.obsidian_cost[0], f.geode_cost[0])
        highest_clay_cost = f.obsidian_cost[1]

        max_geodes = 0
        while len(q) > 0:
            next = q.pop(-1)
            if next in seen:
                continue

            (ts, ore_robots, clay_robots, obsidian_robots, geode_robots,
             ore, clay, obsidian, geode) = next 

            if ts == 24:
                max_geodes = max(max_geodes, geode)
                continue

            if geode >= geode_memos[ts]:
                geode_memos[ts] = geode
            elif geode_memos[ts] > 0:
                continue

            # print(f"ts: {ts}, ore: {ore}, clay: {clay}, obsidian: {obsidian}, geode: {geode}, ore_robots: {ore_robots}, clay_robots: {clay_robots}, obsidian_robots: {obsidian_robots}, geode_robots: {geode_robots}")

            # Collect new ore (but don't actually add until later)
            new_ore = ore + ore_robots
            new_clay = clay + clay_robots
            new_obsidian = obsidian + obsidian_robots
            new_geode = geode + geode_robots

            # Decide whether to spend materials to build a new robot
            if f.ore_cost <= ore and ts < 20 and ore < highest_ore_cost:
                q.append((ts+1, ore_robots+1, clay_robots, obsidian_robots, geode_robots,
                          new_ore-f.ore_cost, new_clay, new_obsidian, new_geode))
            if f.clay_cost <= ore and ts < 21 and clay < highest_clay_cost:
                q.append((ts+1, ore_robots, clay_robots+1, obsidian_robots, geode_robots,
                          new_ore-f.clay_cost, new_clay, new_obsidian, new_geode))
            if f.obsidian_cost[0] <= ore and f.obsidian_cost[1] <= clay:
                q.append((ts+1, ore_robots, clay_robots, obsidian_robots+1, geode_robots, 
                    new_ore-f.obsidian_cost[0], new_clay-f.obsidian_cost[1], new_obsidian, new_geode))
            if f.geode_cost[0] <= ore and f.geode_cost[1] <= obsidian:
                q.append((ts+1, ore_robots, clay_robots, obsidian_robots, geode_robots+1, 
                    new_ore-f.geode_cost[0], new_clay, new_obsidian-f.geode_cost[1], new_geode))

            # Also consider building no robots
            # it doesn't make sense to store up more ore than is needed for the highest ore cost robot
            q.append((ts+1, ore_robots, clay_robots, obsidian_robots,
                                 geode_robots, new_ore, new_clay, new_obsidian, new_geode))

        print("max", max_geodes)
        score += ((fi+1)*max_geodes)
        print(score)

    print(score)


if __name__ == "__main__":
    main(argv[1])
