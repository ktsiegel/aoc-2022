from sys import argv


def main(filename):
    # Read the input file
    with open(filename, "r") as f:
        input = [int(x.strip()) for x in f.readlines()]

    nums = []
    for i in range(len(input)):
        nums.append((input[i], i))

    for i in range(len(input)):
        j = 0
        while j < len(nums):
            if nums[j][1] == i:
                # print("moving " + str(nums[j]))
                num = nums.pop(j)
                new_idx = j + (num[0])
                # print(j)
                # print(new_idx)
                # print(new_idx, new_idx % len(input))
                if new_idx < 0:
                    while new_idx < 0:
                        new_idx += len(input)-1
                elif new_idx == 0:
                    new_idx = len(input)-1
                elif new_idx > len(input):
                    while new_idx > len(input):
                        new_idx -= len(input)-1

                nums.insert(new_idx, num)
                break

            j += 1

    pp = []
    for i in nums:
        pp.append(i[0])
    print(pp)

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
