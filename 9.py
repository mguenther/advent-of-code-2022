FILENAME = '9.in'
DIRECTIONS = {
    'L': (-1, 0),
    'R': (1, 0),
    'U': (0, 1),
    'D': (0, -1)
}


def delta(head, tail):
    return (head[0] - tail[0], head[1] - tail[1])


def value(delta):
    return abs(delta[0]) + abs(delta[1])


def is_close(delta):
    d = (abs(delta[0]), abs(delta[1]))
    return d == (1, 1) or value(delta) < 2


def walk(movements, knots):
    head = (0, 0)
    visited = set()
    for movement in movements:
        tokens = movement.split()
        direction, amount = tokens[0], int(tokens[1])
        for _ in range(amount):
            d = DIRECTIONS[direction]
            head = (head[0] + d[0], head[1] + d[1])
            predecessor = head
            for i, knot in enumerate(knots):
                delta_to_predecessor = delta(predecessor, knot)
                if not(is_close(delta_to_predecessor)):
                    dx = min(1, delta_to_predecessor[0]) if delta_to_predecessor[0] >= 0 else max(-1, delta_to_predecessor[0])
                    dy = min(1, delta_to_predecessor[1]) if delta_to_predecessor[1] >= 0 else max(-1, delta_to_predecessor[1])
                    knots[i] = (knot[0] + dx, knot[1] + dy)
                predecessor = knots[i]
            visited.add(predecessor)
    return len(visited)


movements = [l.strip() for l in open(FILENAME, 'r').readlines()]
subsequent_knots_part_1 = [(0, 0)]
subsequent_knots_part_2 = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]

print(walk(movements, subsequent_knots_part_1))
print(walk(movements, subsequent_knots_part_2))
