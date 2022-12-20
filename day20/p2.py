from sys import argv
from math import floor


decode = 811589153


def main(filename):
    # Read the input file
    with open(filename, "r") as f:
        input = [int(x.strip()) for x in f.readlines()]

    nums = []
    for i in range(len(input)):
        nums.append((input[i]*decode, i))

    for t in range(10):
        for i in range(len(input)):
            j = 0
            while j < len(nums):
                if nums[j][1] == i:
                    num = nums.pop(j)
                    new_idx = j + (num[0])
                    if new_idx < 0 or new_idx > len(input)-1:
                        new_idx %= len(input)-1
                    elif new_idx == 0:
                        new_idx = len(input)-1

                    nums.insert(new_idx, num)
                    break

                j += 1

    for i in range(len(input)):
        if nums[i][0] == 0:
            zero_idx = i
            break
    x = nums[(zero_idx+1000) % len(input)][0]
    y = nums[(zero_idx+2000) % len(input)][0]
    z = nums[(zero_idx+3000) % len(input)][0]
    print(str(x + y + z))


if __name__ == "__main__":
    main(argv[1])
