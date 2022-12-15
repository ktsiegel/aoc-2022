from sys import argv
from math import floor, lcm


class Monkey:
    def __init__(self, items, op, op_on_self, operand, divisible_test, if_true, if_false):
        self.items = items
        self.op = op
        self.op_on_self = op_on_self
        self.operand = operand
        self.divisible_test = divisible_test
        self.if_true = if_true  # monkey to go to if true
        self.if_false = if_false  # monkey to go to if false

    def __str__(self):
        return str(self.items)

    def operation(self, item):
        if self.op == "+":
            if self.op_on_self:
                return item + item
            else:
                return item + self.operand
        elif self.op == "*":
            if self.op_on_self:
                return item * item
            else:
                return item * self.operand
        else:
            raise Exception("Unknown operation: " + op)


def main(filename):
    # Read the input file
    with open(filename, "r") as f:
        input = [x.strip() for x in f.readlines()]

    i = 0
    monkeys = []
    while i < len(input):
        [txt, starting_items_str] = input[i+1].split(": ")
        starting_items = [int(x.strip())
                          for x in starting_items_str.split(", ")]

        [txt, operation_str] = input[i+2].split(": ")
        equation = operation_str.strip().split(" ")
        operation_num = equation[-1].strip()
        op = equation[-2].strip()

        # always a divisible test
        divisible_test = int(input[i+3].split(" ")[-1].strip())

        if_true_test = int(input[i+4].split(" ")[-1].strip())
        if_false_test = int(input[i+5].split(" ")[-1].strip())

        operand = 0
        if operation_num != "old":
            operand = int(operation_num)
        monkeys.append(Monkey(starting_items, op, operation_num == "old", operand,
                       divisible_test, if_true_test, if_false_test))

        i += 7

    inspection_counts = [0] * len(monkeys)

    # find the least common multiple of the divisible tests
    mul = monkeys[0].divisible_test
    for monkey in monkeys[1:]:
        mul = lcm(mul, monkey.divisible_test)

    max_rounds = 10000
    round = 0
    while round < max_rounds:
        for monkey_index in range(len(monkeys)):
            monkey = monkeys[monkey_index]
            while len(monkey.items) > 0:
                item = monkey.items.pop(0)
                inspection_counts[monkey_index] += 1

                item = int(floor(monkey.operation(item)))
                item = item % mul
                if item % monkey.divisible_test == 0:
                    monkeys[monkey.if_true].items.append(item)
                else:
                    monkeys[monkey.if_false].items.append(item)

        round += 1

    inspection_counts.sort()
    print(inspection_counts[-1] * inspection_counts[-2])


if __name__ == "__main__":
    main(argv[1])
