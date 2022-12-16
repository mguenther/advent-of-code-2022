from itertools import pairwise


DEBUG = False
FILENAME = '14.in'
MAX_WIDTH = 700


def parse(filename):
    return [[tuple([int(coordinate) for coordinate in segment.split(',')]) for segment in l.strip().split(' -> ')] for l in open(filename, 'r')]


def compute_max_y(traces):
    ys = []
    for trace in traces:
        for _, y in trace:
            ys.append(y)
    return max(ys)


def build_grid(filename):
    G = [['.' for _ in range(0, MAX_WIDTH)] for _ in range(0, 161)]
    traces = parse(filename)
    max_y = compute_max_y(traces)

    for x in range(0, MAX_WIDTH):
        G[max_y + 2][x] = '#'

    rocks = []
    for trace in traces:
        for l, r in pairwise(trace):
            x1, y1 = l
            x2, y2 = r
            if x1 <= x2:
                for dx in range(x1, x2 + 1):
                    if y1 <= y2:
                        for dy in range(y1, y2 + 1):
                            rocks.append((dx, dy))
                    else:
                        for dy in range(y1, y2 - 1, -1):
                            rocks.append((dx, dy))
            else:
                for dx in range(x1, x2 - 1, -1):
                    if y1 <= y2:
                        for dy in range(y1, y2 + 1):
                            rocks.append((dx, dy))
                    else:
                        for dy in range(y1, y2 - 1, -1):
                            rocks.append((dx, dy))

    for rock in rocks:
        G[rock[1]][rock[0]] = '#'

    return G, max_y


def continues_1st(_, max_y, sand):
    return sand[1] <= max_y


def continues_2nd(G, _, sand):
    return G[sand[1]][sand[0]] == '.'


def compute_units_of_sand_until(filename, probe_fn):
    G, max_y = build_grid(filename)
    units_of_sand = 0
    tick = 0
    sand = (500, 0)
    while probe_fn(G, max_y, sand):
        if G[sand[1] + 1][sand[0]] == '.':
            sand = (sand[0], sand[1] + 1)
        else:
            if G[sand[1] + 1][sand[0] - 1] == '.':
                sand = (sand[0] - 1, sand[1] + 1)
            elif G[sand[1] + 1][sand[0] + 1] == '.':
                sand = (sand[0] + 1, sand[1] + 1)
            else:
                G[sand[1]][sand[0]] = 'o'
                sand = (500, 0)
                units_of_sand += 1
        tick += 1
    if DEBUG:
        for i, row in enumerate(G):
            print(''.join(row))
    return units_of_sand


print(compute_units_of_sand_until(FILENAME, continues_1st))
print(compute_units_of_sand_until(FILENAME, continues_2nd))