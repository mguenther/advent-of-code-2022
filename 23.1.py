FILENAME = '23.in'
POSSIBLE_MOVES = [(0, -1), (0, 1), (-1, 0), (1, 0)]
NEIGHBOURS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
CLEARANCE_BY_MOVE = {
    (0, -1): [(-1, -1), (0, -1), (1, -1)], # check NW, N, NE in order to propose a move to N
    (0, 1) : [(-1, 1), (0, 1), (1, 1)],    # check SW, S, SE in order to propose a move to S
    (-1, 0): [(-1, 0), (-1, -1), (-1, 1)], # check W, NW, SW in order to propose a move to W
    (1, 0) : [(1, 0), (1, -1), (1, 1)],    # check E, NE, SE in order to propose a move to E
}


def parse(filename):
    lines = [l.strip() for l in open(filename, 'r').readlines()]
    elves = set()
    for row, line in enumerate(lines):
        for col, field in enumerate(line):
            if field == '#':
                elves.add((col, row))
    return elves


elves = parse(FILENAME)

for _ in range(10):
    once = set()
    twice = set()
    for elf in elves:
        abs_neighbours = [(elf[0] + dx, elf[1] + dy) for (dx, dy) in NEIGHBOURS]
        is_isolated = all(neighbour not in elves for neighbour in abs_neighbours)
        if is_isolated:
            continue
        for move in POSSIBLE_MOVES:
            probe_moves = [(elf[0] + dx, elf[1] + dy) for (dx, dy) in CLEARANCE_BY_MOVE[move]]
            is_clear = all(np not in elves for np in probe_moves)
            if is_clear:
                prop = (elf[0] + move[0], elf[1] + move[1])
                if prop in twice:
                    pass
                elif prop in once:
                    twice.add(prop)
                else:
                    once.add(prop)
                break

    elves_clone = set(elves)

    for elf in elves_clone:
        abs_neighbours = [(elf[0] + dx, elf[1] + dy) for (dx, dy) in NEIGHBOURS]
        is_isolated = all(neighbour not in elves_clone for neighbour in abs_neighbours)
        if is_isolated:
            continue
        for move in POSSIBLE_MOVES:
            probe_moves = [(elf[0] + dx, elf[1] + dy) for (dx, dy) in CLEARANCE_BY_MOVE[move]]
            is_clear = all(np not in elves_clone for np in probe_moves)
            if is_clear:
                prop = (elf[0] + move[0], elf[1] + move[1])
                if prop not in twice:
                    elves.remove(elf)
                    elves.add(prop)
                break
    
    POSSIBLE_MOVES.append(POSSIBLE_MOVES.pop(0))

min_x = min(elf[0] for elf in elves)
max_x = max(elf[0] for elf in elves)
min_y = min(elf[1] for elf in elves)
max_y = max(elf[1] for elf in elves)

box = (max_x - min_x + 1) * (max_y - min_y + 1)
print(box - len(elves))