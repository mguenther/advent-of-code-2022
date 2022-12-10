FILENAME = '10.in'
PROBE_AT_CYCLE = [20, 60, 100, 140, 180, 220]


def row(cycle):
    return cycle // 40


def column(cycle):
    return cycle % 40


def pixel(cycle, sprite_pos):
    return '#' if (cycle % 40) in sprite_pos else ' '


program = [l.strip() for l in open(FILENAME, 'r').readlines()]
signal_strengths = []
pixels = [['X' for _ in range(40)] for _ in range(7)]
sprite_pos = [1, 2, 3]
x = 1
cycle = 0
for statement in program:
    already = False
    if statement.startswith('noop'):
        cycle += 1
        pixels[row(cycle)][column(cycle)] = pixel(cycle, sprite_pos)
    elif statement.startswith('addx'):
        command, argument = statement.split()
        argument = int(argument)
        for _ in range(2):
            cycle += 1
            pixels[row(cycle)][column(cycle)] = pixel(cycle, sprite_pos)
            if cycle in PROBE_AT_CYCLE:
                signal_strengths.append(cycle * x)
                already = True
        x += argument
        sprite_pos = [x, x + 1, x + 2]
    if not already and cycle in PROBE_AT_CYCLE:
        signal_strengths.append(cycle * x)
        pixels[row(cycle)][column(cycle)] = pixel(cycle, sprite_pos)

print(sum(signal_strengths))

for row in pixels:
    print(''.join(row))