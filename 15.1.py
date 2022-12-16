from collections import defaultdict


FILENAME = '15.in'


def manhattan_distance(s, b):
    sx, sy = s
    bx, by = b
    return abs(sx - bx) + abs(sy - by)


def solve(filename):
    lls = defaultdict(list)
    lines = [l.strip() for l in open(filename, 'r').readlines()]
    for line in lines:
        tokens = line.split()
        sx = int(tokens[2].split('=')[1][:-1])
        sy = int(tokens[3].split('=')[1][:-1])
        bx = int(tokens[8].split('=')[1][:-1])
        by = int(tokens[9].split('=')[1])

        d = manhattan_distance((sx, sy), (bx, by))
        for dx in range(d):
            dy = abs(d - dx)
            row_1 = sy + dy
            row_2 = sy - dy
            lls[row_1].append((sx - dx, sx + dx))
            lls[row_2].append((sx - dx, sx + dx))

    c = set()
    l = lls[2000000]
    for start, end in l:
        for x in range(start, end):
            c.add(x)
    print(len(c))


solve(FILENAME)