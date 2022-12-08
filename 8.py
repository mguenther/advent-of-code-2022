from functools import reduce


FILENAME = '8.in'
DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def solve_first_part(height_map):
    visible_count = 0
    for x in range(0, len(height_map)):
        for y in range(0, len(height_map)):
            h = height_map[x][y]
            for dx, dy in DIRECTIONS:
                nx = x
                ny = y
                visible = True
                while True:
                    nx += dx
                    ny += dy
                    if (nx < 0 or ny < 0 or nx == len(height_map) or ny == len(height_map)):
                        break
                    probe_h = height_map[nx][ny]
                    visible = h > probe_h
                    if not(visible):
                        break

                if visible:
                    visible_count += 1
                    break
    return visible_count


def solve_second_part(height_map):
    highest_scenic_score = 0
    for x in range(1, len(height_map)-1):
        for y in range(1, len(height_map)-1):
            h = height_map[x][y]
            scores = []
            for dx, dy in DIRECTIONS:
                nx = x
                ny = y
                score = 0
                while True:
                    nx += dx
                    ny += dy
                    if (nx < 0 or ny < 0 or nx == len(height_map) or ny == len(height_map)):
                        break
                    score += 1
                    probe_h = height_map[nx][ny]
                    if not(h > probe_h):
                        break
                scores.append(score)
            scenic_score = reduce(lambda x, y: x * y, scores)
            if scenic_score > highest_scenic_score:
                highest_scenic_score = scenic_score
    return highest_scenic_score
                

height_map = [[int(h) for h in l.strip()] for l in open(FILENAME, 'r').readlines()]

print(solve_first_part(height_map))
print(solve_second_part(height_map))