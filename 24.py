from collections import deque


FILENAME = '24.in'
MOVEMENTS = [(0, 1), (0, -1), (-1, 0), (1, 0), (0, 0)]
MOVEMENTS_BLIZZARD = [(0, 0, -1), (1, 0, 1), (2, -1, 0), (3, 1, 0)]


def parse_blizzards(filename):
    blizzards = tuple(set() for _ in range(4))
    for row, line in enumerate(open(filename).readlines()[1:]):
        for column, item in enumerate(line[1:]):
            if item in '<>^v':
                blizzards['<>^v'.find(item)].add((row, column))
    return blizzards, row, column


def solve_part_one(filename):
    blizzards, number_of_rows, number_of_columns = parse_blizzards(filename)
    # Q holds the fringe of the search space
    # we start off at the initial position
    Q = deque([(0, -1, 0)])
    # S holds states that we have already processed
    S = set()
    target = (number_of_rows, number_of_columns - 1)

    while Q:
        time, current_row, current_column = Q.popleft()
        time += 1

        for delta_row, delta_column in MOVEMENTS:
            next_row = current_row + delta_row
            next_column = current_column + delta_column
            if (next_row, next_column) == target:
                return time
            if (next_row < 0 or next_column < 0 or next_row >= number_of_rows or next_column >= number_of_columns) and not (next_row, next_column) == (-1, 0):
                continue
            fail = False
            if (next_row, next_column) != (-1, 0):
                for i, tr, tc in MOVEMENTS_BLIZZARD:
                    # check if we collide with a blizzard
                    # if we do, we break out of the for-loop and discontinue processing that state
                    # if we don't, we might have a successor state to process (if we haven't already
                    # seen that state)
                    if ((next_row - tr * time) % number_of_rows, (next_column - tc * time) % number_of_columns) in blizzards[i]:
                        fail = True
                        break
            if not fail:
                key = (next_row, next_column, time)
                if (key in S):
                    continue
                S.add(key)
                Q.append((time, next_row, next_column))


def solve_part_two(filename):
    blizzards, number_of_rows, number_of_columns = parse_blizzards(filename)
    # Q holds the fringe of the search space
    # we start off at the initial position
    Q = deque([(0, -1, 0, 0)])
    # S holds states that we have already processed
    S = set()
    targets = [(number_of_rows, number_of_columns - 1), (-1, 0)]

    while Q:
        time, current_row, current_column, stage = Q.popleft()
        time += 1

        for delta_row, delta_column in MOVEMENTS:
            next_row = current_row + delta_row
            next_column = current_column + delta_column
            next_stage = stage
            if (next_row, next_column) == targets[stage % 2]:
                if stage == 2:
                    print(time)
                    exit(0)
                else:
                    next_stage += 1
            if (next_row < 0 or next_column < 0 or next_row >= number_of_rows or next_column >= number_of_columns) and (next_row, next_column) not in targets:
                continue
            fail = False
            if (next_row, next_column) != (-1, 0):
                for i, tr, tc in MOVEMENTS_BLIZZARD:
                    # check if we collide with a blizzard
                    # if we do, we break out of the for-loop and discontinue processing that state
                    # if we don't, we might have a successor state to process (if we haven't already
                    # seen that state)
                    if ((next_row - tr * time) % number_of_rows, (next_column - tc * time) % number_of_columns) in blizzards[i]:
                        fail = True
                        break
            if not fail:
                key = (next_row, next_column, next_stage, time)
                if (key in S):
                    continue
                S.add(key)
                Q.append((time, next_row, next_column, next_stage))


print(solve_part_one(FILENAME))
print(solve_part_two(FILENAME))