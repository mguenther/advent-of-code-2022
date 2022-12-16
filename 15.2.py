# got stuck on part 2 with my initial approach, so I researched
# for a bit and found a great explanation by William Y. Feng
# (see https://www.youtube.com/watch?v=w7m48_uCvWI), which helped
# me out a lot


FILENAME = '15.in'


def manhattan_distance(s, b):
    sx, sy = s
    bx, by = b
    return abs(sx - bx) + abs(sy - by)


lines = [l.strip() for l in open(FILENAME, 'r').readlines()]
sensors = []
dists = []
for line in lines:
    tokens = line.split()
    sx = int(tokens[2].split('=')[1][:-1])
    sy = int(tokens[3].split('=')[1][:-1])
    bx = int(tokens[8].split('=')[1][:-1])
    by = int(tokens[9].split('=')[1])
    sensors.append((sx, sy))
    d = manhattan_distance((sx, sy), (bx, by))
    dists.append(d)


N = len(sensors)

pos_lines = []
neg_lines = []

for i, s in enumerate(sensors):
    d = dists[i]
    neg_lines.extend([s[0] + s[1] - d, s[0] + s[1] + d])
    pos_lines.extend([s[0] - s[1] - d, s[0] - s[1] + d])

pos = None
neg = None

for i in range(2 * N):
    for j in range(i + 1, 2 * N):
        a, b = pos_lines[i], pos_lines[j]

        if abs(a - b) == 2:
            pos = min(a, b) + 1

        a, b = neg_lines[i], neg_lines[j]

        if abs(a - b) == 2:
            neg = min(a, b) + 1


x, y = (pos + neg) // 2, (neg - pos) // 2
ans = x * 4000000 + y
print(ans)