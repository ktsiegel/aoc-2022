from sys import argv


def main(filename):
    # Read the input file
    with open(filename, "r") as f:
        input = [x.strip() for x in f.readlines()]

    h = [0,0] # r,c
    t = [0,0]
    visited = set()
    for l in input:
        [dir, steps] = l.split(' ')
        steps = int(steps)
        for i in range(steps):
            if dir == "R":
                # column moves
                h[1] += 1
            if dir == "L":
                h[1] -= 1
            if dir == "U":
                h[0] += 1
            if dir == "D":
                h[0] -= 1
        
            if h[0] == t[0]:
                if h[1] > t[1]:
                    t[1] = h[1]-1
                elif h[1] < t[1]:
                    t[1] = h[1]+1
            elif h[1] == t[1]:
                if h[0] > t[0]:
                    t[0] = h[0]-1
                elif h[0] < t[0]:
                    t[0] = h[0]+1
            elif abs(h[0]-t[0]) >1 or abs(h[1]-t[1]) > 1:
                if h[0] < t[0] and h[1] < t[1]:
                    # first quadrant
                    t = [t[0]-1, t[1]-1]
                elif h[0] < t[0] and h[1] > t[1]:
                    # second quadrant
                    t = [t[0]-1, t[1]+1]
                elif h[0] > t[0] and h[1] > t[1]:
                    # third quadrant
                    t = [t[0]+1, t[1]+1]
                else:
                    # fourth quadrant
                    t = [t[0]+1, t[1]-1]
            visited.add(tuple(t))
    print(len(visited))




if __name__ == "__main__":
    main(argv[1])

        