from sys import argv


class Sensor:
    def __init__(self, loc, beacon_loc):
        self.loc = loc
        self.beacon_loc = beacon_loc
        self.dist = abs(loc[0]-beacon_loc[0]) + abs(loc[1]-beacon_loc[1])

    def __str__(self):
        return "Sensor at {}, beacon at {}".format(self.loc, self.beacon_loc)


def merge_ranges(ranges):
    merged_ranges = []
    for r in ranges:
        if len(merged_ranges) == 0:
            merged_ranges.append(r)
        else:
            if r[0] <= merged_ranges[-1][1]+1:
                merged_ranges[-1][1] = max(merged_ranges[-1][1], r[1])
            else:
                merged_ranges.append(r)
    return merged_ranges


def main(filename):
    # Read the input file
    with open(filename, "r") as f:
        input = [x.strip().split(" ") for x in f.readlines()]

    sensors = []
    beacon_target_xs = dict()
    for line in input:
        x = int(line[2].split("=")[1][0:-1])
        y = int(line[3].split("=")[1][0:-1])
        beacon_x = int(line[8].split("=")[1][0:-1])
        beacon_y = int(line[9].split("=")[1])
        if beacon_x in beacon_target_xs:
            beacon_target_xs[beacon_x].add(beacon_y)
        else:
            beacon_target_xs[beacon_x] = set([beacon_y])
        sensor = Sensor((x, y), (beacon_x, beacon_y))
        sensors.append(sensor)

    max_dim = 4000000
    blocked_ys = dict()
    for sensor in sensors:
        for target_y in range(sensor.loc[1]-sensor.dist, sensor.loc[1]+sensor.dist+1):
            if target_y < 0 or target_y > max_dim:
                continue
            if target_y not in blocked_ys:
                blocked_ys[target_y] = []
            diff = sensor.dist - abs(sensor.loc[1]-target_y)
            blocked_range = [max(0, sensor.loc[0]-diff),
                             min(sensor.loc[0]+diff, max_dim)]

            blocked_ys[target_y].append(blocked_range)
            blocked_ys[target_y].sort()
            blocked_ys[target_y] = merge_ranges(blocked_ys[target_y])

    for blocked_y in blocked_ys:
        if len(blocked_ys[blocked_y]) > 1:
            print(blocked_y, blocked_ys[blocked_y])
            y = blocked_y
            x = blocked_ys[y][0][1]+1
            print(x*4000000+y)


if __name__ == "__main__":
    main(argv[1])
