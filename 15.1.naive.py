from collections import defaultdict


FILENAME = '15.test.in'


def manhattan_distance(s, b):
    sx, sy = s
    bx, by = b
    return abs(sx - bx) + abs(sy - by)


def solve(filename):
    p = set() # belongs to the naive approach
    lines = [l.strip() for l in open(filename, 'r').readlines()]
    for line in lines:
        tokens = line.split()
        sx = int(tokens[2].split('=')[1][:-1])
        sy = int(tokens[3].split('=')[1][:-1])
        bx = int(tokens[8].split('=')[1][:-1])
        by = int(tokens[9].split('=')[1])
        d = manhattan_distance((sx, sy), (bx, by))
        # correct, but slow, as it enumerates all individual points
        # don't use this with the actual problem set
        for dx in range(-d, d + 1):
            for dy in range(-d + dx, d + 1 - dx):
                if abs(dx) + abs(dy) > d:
                    continue
                cx = sx + dx
                cy = sy + dy
                if (cx, cy) == (sx, sy) or (cx, cy) == (bx, by):
                    continue
                p.add((cx, cy))

    c = 0
    for _, y in p:
        if y == 10:
            c += 1
    print(c)


solve(FILENAME)