from collections import deque


FILENAME = '12.in'
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def determine_start(M):
    rows = len(M)
    cols = len(M[0])
    for row in range(rows):
        for col in range(cols):
            if M[row][col] == 'S':
                return [((row, col), 0)]
    return [((None, None), None)]


def determine_start_2nd(M):
    result = []
    rows = len(M)
    cols = len(M[0])
    for row in range(rows):
        for col in range(cols):
            if M[row][col] == 'a':
                result.append(((row, col), 0))
    return result


def build_height_map(M):
    rows = len(M)
    cols = len(M[0])
    height_map = [[0 for _ in range(cols)] for _ in range(rows)]
    for row in range(rows):
        for col in range(cols):
            if M[row][col] == 'S':
                height_map[row][col] = 1
            elif M[row][col] == 'E':
                height_map[row][col] = 26
            else:
                height_map[row][col] = ord(M[row][col]) - ord('a') + 1
    return height_map


def minimum_steps_required(S):
    steps_required = []
    for s in S:
        Q = deque()
        Q.append(s)
        S = set()
        while Q:
            (row, col), steps = Q.popleft()

            if (row, col) in S:
                continue

            S.add((row, col))

            if M[row][col] == 'E':
                steps_required.append(steps)
                break

            for delta_row, delta_col in DIRECTIONS:
                next_row = row + delta_row
                next_col = col + delta_col
                if 0 <= next_row < len(M) and 0 <= next_col < len(M[0]) and height_map[next_row][next_col] <= 1 + height_map[row][col]:
                    Q.append(((next_row, next_col), steps + 1))
    return min(steps_required)


M = [l.strip() for l in open(FILENAME, 'r').readlines()]

height_map = build_height_map(M)

print(minimum_steps_required(determine_start(M)))
print(minimum_steps_required(determine_start_2nd(M)))