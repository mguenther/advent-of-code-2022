FILENAME = '3.in'


def value(c):
    if c.islower():
        return ord(c) - ord('a') + 1
    else:
        return ord(c) - ord('A') + 26 + 1


def split(s):
    l = len(s)
    return (s[slice(0,l//2)], s[slice(l//2,l)])


def intersect2(x, y):
    return set(x).intersection(set(y)).pop()


def intersect3(x, y, z):
    return set(x).intersection(set(y).intersection(set(z))).pop()


def solve_first_part(rucksacks):
    rucksacks = [split(l) for l in rucksacks]
    sum = 0
    for x, y in rucksacks:
        sum += value(intersect2(x, y))
    return sum


def solve_second_part(rucksacks):
    l = [rucksacks[x:x+3] for x in range(0, len(rucksacks), 3)]
    sum = 0
    for x, y, z in l:
        sum += value(intersect3(x, y, z))
    return sum


rucksacks = [l.strip() for l in open(FILENAME, 'r').readlines()]

print(solve_first_part(rucksacks))
print(solve_second_part(rucksacks))