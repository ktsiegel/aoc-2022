from sys import argv
from enum import Enum


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


def main(filename):
    # Read the input file
    with open(filename, "r") as f:
        factories = [Factory(x.strip()) for x in f.readlines()]

    # (robots, resources) -- ore, clay, obsidian, geode
    q = [(0, [1, 0, 0, 0], [0, 0, 0, 0])]

    geode_robot_memos = [0]*24

    f = factories[0]
    max_geodes = 0
    while len(q) > 0:
        (ts, [ore_robots, clay_robots, obsidian_robots, geode_robots],
         [ore, clay, obsidian, geode]) = q.pop(0)

        if ts == 24:
            max_geodes = max(max_geodes, geode)
            continue

        # print(f"ts: {ts}, ore: {ore}, clay: {clay}, obsidian: {obsidian}, geode: {geode}, ore_robots: {ore_robots}, clay_robots: {clay_robots}, obsidian_robots: {obsidian_robots}, geode_robots: {geode_robots}")
        if geode_robots > geode_robot_memos[ts]:
            geode_robot_memos[ts] = geode_robots
        elif geode_robot_memos[ts] > 0:
            continue

        # Collect new ore (but don't actually add until later)
        new_ore = ore + ore_robots
        new_clay = clay + clay_robots
        new_obsidian = obsidian + obsidian_robots
        new_geode = geode + geode_robots

        # Decide whether to spend materials to build a new robot
        if f.ore_cost <= ore:
            q.append((ts+1, [ore_robots+1, clay_robots, obsidian_robots, geode_robots],
                     [new_ore-f.ore_cost, new_clay, new_obsidian, new_geode]))
        if f.clay_cost <= ore:
            q.append((ts+1, [ore_robots, clay_robots+1, obsidian_robots, geode_robots],
                     [new_ore, new_clay-f.clay_cost, new_obsidian, new_geode]))
        if f.obsidian_cost[0] <= ore and f.obsidian_cost[1] <= clay:
            q.append((ts+1, [ore_robots, clay_robots, obsidian_robots+1, geode_robots], [
                     new_ore-f.obsidian_cost[0], new_clay-f.obsidian_cost[1], new_obsidian, new_geode]))
        if f.geode_cost[0] <= ore and f.geode_cost[1] <= obsidian:
            q.append((ts+1, [ore_robots, clay_robots, obsidian_robots, geode_robots+1], [
                     new_ore-f.geode_cost[0], new_clay, new_obsidian-f.geode_cost[1], new_geode]))

        # Also consider building no robots
        q.append((ts+1, [ore_robots, clay_robots, obsidian_robots,
                 geode_robots], [new_ore, new_clay, new_obsidian, new_geode]))

    print(max_geodes)


if __name__ == "__main__":
    main(argv[1])
