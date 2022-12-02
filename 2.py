from itertools import permutations


FILENAME = '2.in'

MAPPING = {
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scissors'
}

TURN_SCORING = {
            ('A', 'A'): 1 + 3,
            ('A', 'B'): 1 + 0,
            ('A', 'C'): 1 + 6,
            ('B', 'A'): 2 + 6,
            ('B', 'B'): 2 + 3,
            ('B', 'C'): 2 + 0,
            ('C', 'A'): 3 + 0,
            ('C', 'B'): 3 + 6,
            ('C', 'C'): 3 + 3
}

moves = [move.strip().split(' ') for move in open(FILENAME, 'r').readlines()]

MAP = {
    'Y': 'B',
    'X': 'A',
    'Z': 'C'
}

score = 0

for move in moves:
    opponent_move = move[0]
    our_move = MAP[move[1]]
    score += TURN_SCORING[(our_move, opponent_move)]

print(MAP, score)

MAP_2 = {
    ('A', 'X'): 'C',
    ('B', 'X'): 'A',
    ('C', 'X'): 'B',
    ('A', 'Y'): 'A',
    ('B', 'Y'): 'B',
    ('C', 'Y'): 'C',
    ('A', 'Z'): 'B',
    ('B', 'Z'): 'C',
    ('C', 'Z'): 'A'
}

score_2 = 0

for move in moves:
    opponent_move = move[0]
    our_strategy = move[1]
    our_move = MAP_2[(opponent_move, our_strategy)]
    score_2 += TURN_SCORING[(our_move, opponent_move)]

print(score_2)

# (A,X) -> C
# (B,X) -> A
# (C,X) -> B
# (A,Y) -> A
# (B,Y) -> B
# (C,Y) -> C
# (A,Z) -> B
# (B,Z) -> C
# (C,Z) -> A

# X -> lose
# Y -> draw
# Z -> win