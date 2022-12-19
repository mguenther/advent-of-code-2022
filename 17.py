DEBUG = False
FILENAME = '17.in'
OP_LEFT = (-1, 0)
OP_RIGHT = (1, 0)
OP_DOWN = (0, -1)
EXPECTED_NUMBER_OF_ROCKS = 2022
WIDTH = 7


def draw(elem, P):
    max_y = 0
    for _, py in P:
        max_y = max(max_y, py)
    for _, py in elem:
        max_y = max(max_y, py)
    for r in range(max_y + 2, -1, -1):
        rs = ''
        for c in range(WIDTH):
            p = (c, r)
            if p in P:
                rs += '#'
            elif p in elem:
                rs += '@'
            else:
                rs += '.'
        print(rs)


def is_inbound(element, P):
    return all(p[0] >= 0 for p in element) and all(p[0] < WIDTH for p in element) and all(not(p in P) for p in element)# and all(p[1] >= 0 for p in element)


ops = [l.strip() for l in open(FILENAME, 'r').readlines()][0]
k = len(ops)
i = 0

elements = [
    [(0,0),(1,0),(2,0),(3,0)],
    [(1,0),(0,1),(1,1),(2,1),(1,2)],
    [(2,2),(2,1),(0,0),(1,0),(2,0)],
    [(0,0),(0,1),(0,2),(0,3)],
    [(0,0),(1,0),(0,1),(1,1)]
]


P = set()
P.add((0,-1))
P.add((1,-1))
P.add((2,-1))
P.add((3,-1))
P.add((4,-1))
P.add((5,-1))
P.add((6,-1))
element = None
move_down = False
i_ops = 0
i_elem = 0
rock_count = 0
while True:

    if not element:
        element = elements[i_elem % len(elements)]
        dx = 2
        dy = 3
        for px, py in P:
            dy = max(dy, py + 3)
        element = [(p[0] + dx, p[1] + dy) for p in element]
        i_elem += 1
    else:

        if move_down:
            # try to move downwards
            e = [(p[0], p[1] - 1) for p in element]
            if is_inbound(e, P):
                element = e
                if DEBUG:
                    print('Moved element downwards')
            else:
                # is blocked, so make it permanent
                for p in element:
                    P.add(p)
                if DEBUG:
                    print(element, 'became stationary')
                rock_count += 1
                element = None
            move_down = not(move_down)
            if not element:
                element = elements[i_elem % len(elements)]
                dx = 2
                dy = 3
                for px, py in P:
                    dy = max(dy, py + 4)
                element = [(p[0] + dx, p[1] + dy) for p in element]
                if DEBUG:
                    print("New element", element)
                i_elem += 1
            if rock_count == EXPECTED_NUMBER_OF_ROCKS:
                break

        else:
            op = ops[i_ops % len(ops)]
            if op == '<':
                # try to move to the left
                e = [(p[0] - 1, p[1]) for p in element]
                if is_inbound(e, P):
                    element = e
                    if DEBUG:
                        print('Moved', element, 'to the left')
            elif op == '>':
                # try to move to the right
                e = [(p[0] + 1, p[1]) for p in element]
                if is_inbound(e, P):
                    element = e
                    if DEBUG:
                        print('Moved ', element, 'to the right')
            i_ops += 1
            move_down = not(move_down)
    i += 1

    if DEBUG:
        draw(element, P)
        print()

max_y = 0
for _, py in P:
    max_y = max(max_y, py)
# Indices begin from 0, so we have to add 1 to get the
# maximum height of the resulting tower.
print(max_y + 1)