from functools import cmp_to_key, reduce
from math import copysign
from operator import mul


FILENAME = '13.in'


def read(filename):
    result = None
    try:
        with open(filename, 'r') as f:
            result = f.read()
    except IOError:
        print('Unable to read contents of file ' + filename)
    return result


def parse(filename):
    content = read(filename)
    return [tuple([eval(p) for p in pair.split('\n')]) for pair in content.split('\n\n')]


def product(iterable):
    return reduce(mul, iterable, 1)


def both_integers(lhs, rhs):
    return isinstance(lhs, int) and isinstance(rhs, int)


def both_lists(lhs, rhs):
    return isinstance(lhs, list) and isinstance(rhs, list)


def convert_left_hand_side(lhs, rhs):
    return isinstance(lhs, int) and isinstance(rhs, list)


def compare(lhs, rhs):
    if both_integers(lhs, rhs):
        if lhs == rhs:
            return 0
        else:
            return int(copysign(1, lhs - rhs))
    elif both_lists(lhs, rhs):
        i = 0
        while i < len(lhs) and i < len(rhs):
            res = compare(lhs[i], rhs[i])
            if res == -1:
                return -1
            if res == 1:
                return 1
            i += 1
        if i == len(lhs) and i < len(rhs):
            return -1
        elif i == len(rhs) and i < len(lhs):
            return 1
        else:
            return 0
    elif convert_left_hand_side(lhs, rhs):
        return compare([lhs], rhs)
    else:
        return compare(lhs, [rhs])


def solve_part_one(filename):
    score = 0
    for i, (lhs, rhs) in enumerate(parse(filename)):
        res = compare(lhs, rhs)
        if res == -1:
            score += (i + 1)
    return score


def solve_part_two(filename):
    lls = []
    lls.append([[2]]) # insert divider packet #1
    lls.append([[6]]) # insert divider packet #2
    for lhs, rhs in parse(filename):
        lls.append(lhs)
        lls.append(rhs)
    lls = sorted(lls, key=cmp_to_key(compare))
    indices = []
    for i, ll in enumerate(lls):
        if compare([[2]], ll) == 0 or compare([[6]], ll) == 0:
            indices.append(i + 1)
    return product(indices)


print(solve_part_one(FILENAME))
print(solve_part_two(FILENAME))