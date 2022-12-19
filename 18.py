from collections import deque


FILENAME = '18.in'
# This limits the search space for part 2 to a maximum number of iterations
# before the search is terminated while considering the point to be 'outside'.
# If the search space is too limited, then this will yield incorrect results.
# For my input for this day, 1250 seem to work just fine.
SEARCH_SPACE_LIMIT = 1250
M = [(1, 0, 0),(-1, 0, 0),(0, 1, 0),(0, -1, 0),(0, 0, 1),(0, 0, -1)]


def parse(filename):
    cube_positions = [[int(coordinate) for coordinate in l.strip().split(',')] for l in open(filename, 'r').readlines()]
    P = set()
    for cube_position in cube_positions:
        P.add((cube_position[0], cube_position[1], cube_position[2]))
    return P


def number_of_adjacent_cubes(p, P):
    adjacent_cubes = 0
    for m in M:
        if ((p[0] + m[0], p[1] + m[1], p[2] + m[2])) not in P:
            adjacent_cubes += 1
    return adjacent_cubes


def is_likely_outside(p, P):
    # we're doing a BFS here and store adjacent but not yet visited
    # cubes in this queue
    Q = deque()
    Q.append(p)
    # S contains all cubes that we have already visited
    S = set()
    while Q:
        p = Q.popleft()
        if p in P or p in S:
            continue
        S.add(p)
        if len(S) > SEARCH_SPACE_LIMIT:
            return True
        for m in M:
            np = (p[0] + m[0], p[1] + m[1], p[2] + m[2])
            Q.append(np)
    return False


def surface_area(P):
    count = 0
    for p in P:
        count += number_of_adjacent_cubes(p, P)
    return count

def surface_area_only_outside(P):
    count = 0
    for p in P:
        for m in M:
            np = (p[0] + m[0], p[1] + m[1], p[2] + m[2])
            if is_likely_outside(np, P):
                count += 1
    return count


P = parse(FILENAME)

print(surface_area(P))
print(surface_area_only_outside(P))