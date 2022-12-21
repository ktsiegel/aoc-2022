from sys import argv


class Monkey:
    def __init__(self, name, number, first_monkey, op, second_monkey):
        self.name = name
        self.number = number
        self.first_monkey = first_monkey
        self.op = op
        self.second_monkey = second_monkey


def main(filename):
    # Read the input file
    with open(filename, "r") as f:
        input = [x.strip().split(" ") for x in f.readlines()]

    monkeys = dict()
    waiting_on = dict()
    mq = []
    for i in input:
        m = i[0][0:-1]
        digit = None
        first_monkey = None
        second_monkey = None
        op = None
        if len(i) == 2:
            digit = int(i[1])
        else:
            first_monkey = i[1]
            op = i[2]
            second_monkey = i[3]
        monkeys[m] = Monkey(m, digit, first_monkey, op, second_monkey)
        if digit is not None:
            mq.append(m)
        if first_monkey is not None:
            if first_monkey not in waiting_on:
                waiting_on[first_monkey] = []
            waiting_on[first_monkey].append(m)
        if second_monkey is not None:
            if second_monkey not in waiting_on:
                waiting_on[second_monkey] = []
            waiting_on[second_monkey].append(m)

    while len(mq) > 0:
        m = mq.pop(0)
        shouted_monkey = monkeys[m]
        for waiter in waiting_on[m]:
            monkey = monkeys[waiter]
            if monkey.first_monkey == m:
                monkey.first_monkey = shouted_monkey.number
            elif monkey.second_monkey == m:
                monkey.second_monkey = shouted_monkey.number
            if type(monkey.first_monkey) is int and type(monkey.second_monkey) is int:
                if monkey.op == "+":
                    monkey.number = monkey.first_monkey + monkey.second_monkey
                elif monkey.op == "*":
                    monkey.number = monkey.first_monkey * monkey.second_monkey
                elif monkey.op == "-":
                    monkey.number = monkey.first_monkey - monkey.second_monkey
                elif monkey.op == "/":
                    monkey.number = int(
                        monkey.first_monkey / monkey.second_monkey)
                else:
                    raise Exception("oops")
                if waiter == "root":
                    print(monkey.number)
                    return
                mq.append(waiter)


if __name__ == "__main__":
    main(argv[1])
