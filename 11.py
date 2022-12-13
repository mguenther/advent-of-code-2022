import math
import re


DEBUG = False
FILENAME = '11.in'
PATTERN_MONKEY_INDEX = re.compile('Monkey ([0-9]).*')
PATTERN_ITEMS = re.compile('.*Starting items: (.*)')
PATTERN_TEST = re.compile('.*divisible by ([0-9]{1,3})')
PATTERN_THROW_TO = re.compile('.*throw to monkey ([0-9])')


def parse(filename):
    lines = [l.strip() for l in open(filename, 'r').readlines() if l != '\n']
    monkeys = []
    i = 0

    while i < len(lines):
        data = lines[i:i+6]
        n = parse_monkey_index(data[0])
        t = parse_throw_to(data[4])
        f = parse_throw_to(data[5])
        monkey = Monkey(
            n,
            parse_items(data[1]),
            parse_operation(data[2]),
            parse_test(data[3], t, f))
        monkeys.append(monkey)
        i += 6
    return monkeys


def parse_divisible_by(filename):
    list_of_divisible_by = []
    lines = [l.strip() for l in open(filename, 'r').readlines() if l != '\n']
    i = 0
    while i < len(lines):
        data = lines[i:i+6]
        list_of_divisible_by.append(int(PATTERN_TEST.findall(data[3])[0]))
        i += 6
    return list_of_divisible_by


def parse_monkey_index(s):
    return int(PATTERN_MONKEY_INDEX.findall(s)[0])


def parse_items(s):
    raw = PATTERN_ITEMS.findall(s)[0]
    raw = raw.split(',')
    return [int(i.strip()) for i in raw]


def parse_operation(s):
    raw = s.split('new = ')[1]
    raw = raw.replace('old', 'x')
    return lambda x: eval(raw)


def parse_test(s, t, f):
    divide_by = int(PATTERN_TEST.findall(s)[0])
    return lambda x: t if x % divide_by == 0 else f


def parse_throw_to(s):
    return int(PATTERN_THROW_TO.findall(s)[0])


class Monkey(object):

    def __init__(self, index, items, operation_fn, test_fn):
        self._index = index
        self._items = items or []
        self._operation_fn = operation_fn
        self._test_fn = test_fn
        self._inspect_counter = 0

    def accept(self, item):
        self._items.append(item)

    def remove(self, item):
        self._items.remove(item)

    def get_index(self):
        return self._index

    def get_items(self):
        return self._items

    def throw_to(self, bored_level):
        return self._test_fn(bored_level)

    def inspect(self, item):
        self._inspect_counter += 1
        return self._operation_fn(item)

    def times_inspected(self):
        return self._inspect_counter

    def __str__(self):
        return 'Monkey ' + str(self._index) + ' with items ' + ', '.join([str(i) for i in self._items])


def solve_part_one():
    monkeys = parse(FILENAME)
    for round in range(0, 20):
        if DEBUG:
            print('Round ' + str(round))
        for monkey in monkeys:
            if DEBUG:
                print("Monkey " + str(monkey.get_index()) + ":")
            to_be_removed = []
            for item in monkey.get_items():
                worry_level = monkey.inspect(item)
                bored_level = worry_level // 3
                throw_to = monkey.throw_to(bored_level)
                if DEBUG:
                    print("  Monkey inspects an item with a worry level of " + str(item))
                    print("    Worry level is increased to " + str(worry_level))
                    print("    Monkey gets bored with item. Worry level is reduced to " + str(bored_level))
                    print("    Item with worry level " + str(bored_level) + " is thrown to monkey " + str(throw_to))
                monkeys[throw_to].accept(bored_level)
                to_be_removed.append(item)
            for item in to_be_removed:
                monkey.remove(item)
    for monkey in monkeys:
        print(str(monkey.get_index()) + ' inspected items ' + str(monkey.times_inspected()) + ' times.')


def compute_lcm(list_of_divisible_by):
    lcm = 1
    for x in list_of_divisible_by:
        lcm *= (lcm * x) // math.gcd(lcm, x)
    return lcm


def solve_part_two():
    monkeys = parse(FILENAME)
    lcm = compute_lcm(parse_divisible_by(FILENAME))
    for round in range(0, 10000):
        if DEBUG:
            print('Round ' + str(round))
        for monkey in monkeys:
            if DEBUG:
                print("Monkey " + str(monkey.get_index()) + ":")
            to_be_removed = []
            for item in monkey.get_items():
                worry_level = monkey.inspect(item) % lcm
                throw_to = monkey.throw_to(worry_level)
                if DEBUG:
                    print("  Monkey inspects an item with a worry level of " + str(item))
                    print("    Worry level is increased to " + str(worry_level))
                    print("    Monkey gets bored with item. Worry level is reduced to " + str(worry_level))
                    print("    Item with worry level " + str(worry_level) + " is thrown to monkey " + str(throw_to))
                monkeys[throw_to].accept(worry_level)
                to_be_removed.append(item)
            for item in to_be_removed:
                monkey.remove(item)
    for monkey in monkeys:
        print(str(monkey.get_index()) + ' inspected items ' + str(monkey.times_inspected()) + ' times.')


print('Solution to part one:')
print('---------------------')
solve_part_one()
print()
print('Solution to part two:')
print('---------------------')
solve_part_two() # result is: print(eval('166945 * 154173'))