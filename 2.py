from itertools import permutations


FILENAME = '2.in'
# A maps to Rock
# B maps to Paper
# C maps to Scissors
STRATEGY = {
    'Y': 'B',
    'X': 'A',
    'Z': 'C'
}
# X means we are expected to lose
# Y means we are expected to end in a draw
# Z means we are expected to win
STRATEGY_REFINED = {
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
SCORING = {
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


def solve_first_part(moves):

    score = 0

    for move in moves:
        opponent_move = move[0]
        our_move = STRATEGY[move[1]]
        score += SCORING[(our_move, opponent_move)]

    print(score)


def solve_second_part(moves):

    score = 0

    for move in moves:
        opponent_move = move[0]
        our_strategy = move[1]
        our_move = STRATEGY_REFINED[(opponent_move, our_strategy)]
        score += SCORING[(our_move, opponent_move)]

    print(score)


moves = [move.strip().split(' ') for move in open(FILENAME, 'r').readlines()]

solve_first_part(moves)
solve_second_part(moves)