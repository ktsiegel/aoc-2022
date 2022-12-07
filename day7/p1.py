from sys import argv


class TreeNode:
    def __init__(self, name, parent=None, size=0):
        self.name = name
        self.children = []
        self.parent = parent
        self.size = size
    
    def add_child(self, child):
        self.children.append(child)
    
    def p(self, tabs):
        print(" "*tabs + self.name +'' + str(self.size))
        for child in self.children:
            child.p(tabs+1)

def find_large_dirs(tree):
    total = 0
    if tree.size <= 100000 and len(tree.children) > 0:
        total += tree.size
    for child in tree.children:
        total += find_large_dirs(child)
    return total


def main(filename):
    # Read the input file
    with open(filename, "r") as f:
        input = [x.strip() for x in f.readlines()][1:]

    i = 0

    tree = TreeNode("/")
    curr = tree

    while i < len(input):
        if input[i].startswith("$"):
            cmd = input[i].split(" ")
            if cmd[1] == 'cd':
                dir = cmd[2]
                if dir == "/":
                    curr = tree
                elif dir == "..":
                    curr = curr.parent
                else:
                    found_child = False
                    for child in curr.children:
                        if child.name == dir:
                            curr = child
                            found_child = True
                    if not found_child:
                        new = TreeNode(dir, curr)
                        curr.add_child(new)
                        curr = new
                i += 1
            elif cmd[1] == 'ls':
                j = i+1
                while j < len(input) and not input[j].startswith("$"):
                    j+=1
                ls_results = input[i+1:j]
                for result in ls_results:
                    [size_or_dir, name] = result.split(" ")
                    found_child = False
                    for child in curr.children:
                        if child.name == result:
                            found_child = True
                    if not found_child:
                        if size_or_dir == "dir":
                            new = TreeNode(name, curr)
                            curr.add_child(new)
                        else:
                            new = TreeNode(name, curr, int(size_or_dir))
                            curr.add_child(new)
                            ptr = new
                            while ptr.parent is not None:
                                ptr.parent.size += new.size
                                ptr = ptr.parent

                i = j
            else:
                print("Unknown command")
                return
    
    tree.p(0)

    print(find_large_dirs(tree))
                


if __name__ == "__main__":
    main(argv[1])

        