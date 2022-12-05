from copy import deepcopy


FILENAME = '5.in'
STACKS = [
    ['T', 'V', 'J', 'W', 'N', 'R', 'M', 'S'],
    ['V', 'C', 'P', 'Q', 'J', 'D', 'W', 'B'],
    ['P', 'R', 'D', 'H', 'F', 'J', 'B'],
    ['D', 'N', 'M', 'B', 'P', 'R', 'F'],
    ['B', 'T', 'P', 'R', 'V', 'H'],
    ['T', 'P', 'B', 'C'],
    ['L', 'P', 'R', 'J', 'B'],
    ['W', 'B', 'Z', 'T', 'L', 'S', 'C', 'N'],
    ['G', 'S', 'L']
]


def parse_moves():
    moves = []
    commands = [l.strip() for l in open(FILENAME, 'r').readlines()]
    for command in commands:
        t = command.split(' ')
        t = (int(t[1]), int(t[3]) - 1, int(t[5]) - 1)
        moves.append(t)
    return moves


def solve_first_part(moves, stacks):
    for amount, from_stack, to_stack in moves:
        for _ in range(0, amount):
            elem = stacks[from_stack].pop(0)
            stacks[to_stack].insert(0, elem)
    print(''.join(s[0] for s in stacks))


def solve_second_part(moves, stacks):
    for amount, from_stack, to_stack in moves:
        m = stacks[from_stack][:amount]
        stacks[from_stack] = stacks[from_stack][amount:]
        stacks[to_stack] = m + stacks[to_stack]
    print(''.join(s[0] for s in stacks))


solve_first_part(parse_moves(), deepcopy(STACKS))
solve_second_part(parse_moves(), deepcopy(STACKS))