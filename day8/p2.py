from sys import argv


def get_view_score(trees, row, col):
    v1 = 0
    for r in range(row-1, -1, -1):
        v1 += 1
        if trees[r][col] >= trees[row][col]:
            break
    
    v2 = 0
    for r in range(row+1, len(trees)):
        v2+=1
        if trees[r][col] >= trees[row][col]:
            break

    v3 = 0
    for c in range(col-1, -1, -1):
        v3 += 1
        if trees[row][c] >= trees[row][col]:
            break
    
    v4 = 0
    for c in range(col+1, len(trees[row])):
        v4 += 1
        if trees[row][c] >= trees[row][col]:
            break
        
    return v1 * v2 * v3 * v4

def main(filename):
    # Read the input file
    with open(filename, "r") as f:
        input = [x.strip() for x in f.readlines()]

    trees = []
    for row in input:
        treerow = []
        for item in row:
            treerow.append(int(item))
        trees.append(treerow)

    max_score = 0
    for row in range(len(trees)):
        for col in range(len(trees[row])):
            max_score = max(get_view_score(trees, row, col), max_score)

    print(max_score)

if __name__ == "__main__":
    main(argv[1])

        