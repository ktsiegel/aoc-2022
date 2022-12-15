from sys import argv


class Sensor:
    def __init__(self, loc, beacon_loc):
        self.loc = loc
        self.beacon_loc = beacon_loc
        self.dist = abs(loc[0]-beacon_loc[0]) + abs(loc[1]-beacon_loc[1])

    def __str__(self):
        return "Sensor at {}, beacon at {}".format(self.loc, self.beacon_loc)


def main(filename):
    # Read the input file
    with open(filename, "r") as f:
        input = [x.strip().split(" ") for x in f.readlines()]

    sensors = []
    target_y = 2000000
    beacon_target_xs = set()
    for line in input:
        x = line[2].split("=")[1][0:-1]
        y = line[3].split("=")[1][0:-1]
        beacon_x = line[8].split("=")[1][0:-1]
        beacon_y = line[9].split("=")[1]
        if int(beacon_y) == target_y:
            beacon_target_xs.add(int(beacon_x))
        sensor = Sensor((int(x), int(y)), (int(beacon_x), int(beacon_y)))
        sensors.append(sensor)

    blocked_y = set()
    for sensor in sensors:
        dist_from_blocked = abs(sensor.loc[1] - target_y)
        if dist_from_blocked <= sensor.dist:
            i = sensor.loc[0]-(sensor.dist-dist_from_blocked)
            while i <= sensor.loc[0]+(sensor.dist-dist_from_blocked):
                if i not in beacon_target_xs:
                    blocked_y.add(i)
                i += 1
    print(len(blocked_y))

    # for every sensor that has a shadow that overlaps that row
    # add overlap to set


if __name__ == "__main__":
    main(argv[1])
