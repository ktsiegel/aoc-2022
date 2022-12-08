from sys import argv


def check_if_visible(trees, row, col):
    vis = True
    for r in range(0, row):
        if trees[r][col] >= trees[row][col]:
            vis = False
    
    if vis == True:
        return True

    vis = True
    for r in range(row+1, len(trees)):
        if trees[r][col] >= trees[row][col]:
            vis = False

    if vis == True:
        return True

    vis = True
    for c in range(0, col):
        if trees[row][c] >= trees[row][col]:
            vis = False
    
    if vis == True:
        return True

    vis = True
    for c in range(col+1, len(trees[row])):
        if trees[row][c] >= trees[row][col]:
            vis = False
        
    return vis

def main(filename):
    # Read the input file
    with open(filename, "r") as f:
        input = [x.strip() for x in f.readlines()]

    trees = []
    for row in input:
        treerow = []
        for item in row:
            treerow.append(item)
        trees.append(treerow)

    count = 0
    for row in range(len(trees)):
        for col in range(len(trees[row])):
            if check_if_visible(trees, row, col):
                count += 1


    print(count)

if __name__ == "__main__":
    main(argv[1])

        