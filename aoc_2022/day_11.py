"""day 11 of aoc2022"""

import operator
import re
from math import prod


class Monkey:
    def __init__(self, items, rule):
        self.items = items
        self.rule = rule  # [operator,value,divisible,true,false]
        self.inspected = 0

    def inspect(self, item, monkeys, multiple, part):
        result = item

        op, value, divisible, true_branch, false_branch = self.rule

        if op == '+':
            result = item + value
        elif op == '*':
            result = item * value
        elif op == 'sq':
            result = item * item

        if part == 1:
            result = result // 3
        else:
            result = result % multiple

        if result % divisible == 0:
            monkeys[true_branch].items.append(result)
        else:
            monkeys[false_branch].items.append(result)

        self.inspected += 1

    def turn(self, monkeys, multiple, part):
        while len(self.items) > 0:
            current = self.items.pop(0)
            self.inspect(current, monkeys, multiple, part)


def parse_monkeys(data):
    i = iter(data)

    monkeys = []
    while next(i):
        items = [int(m) for m in re.findall(r'[0-9]+', next(i))]
        op_str = next(i)
        op = op_str[23]
        op_with = 0
        if op_str[24:] == ' old':
            op = 'sq'
        else:
            op_with = int(op_str[24:])

        test_str = next(i)
        divisible = int(test_str[21:])
        true_str = next(i)
        true_throw = int(true_str[29:])
        false_str = next(i)
        false_throw = int(false_str[30:])

        monkeys.append(
            Monkey(
                items,
                [op, op_with, divisible, true_throw, false_throw]))

        if next(i, None) is None:
            break

    return monkeys


def day_11(part, data):
    """solve day 11 for the given part and data."""

    monkeys = parse_monkeys(data)
    divs = [m.rule[2] for m in monkeys]
    multiple = prod(divs)

    if part == 1:
        rounds = 20
    else:
        rounds = 10000

    for r in range(rounds):
        for m in monkeys:
            m.turn(monkeys, multiple, part)

    monkeys.sort(key=operator.attrgetter('inspected'))

    return monkeys[-1].inspected * monkeys[-2].inspected
