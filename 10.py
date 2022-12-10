FILENAME = '10.in'


program = [l.strip() for l in open(FILENAME, 'r').readlines()]
signal_strengths = []
pixels = []
sprite_pos = [1, 2, 3]
x = 1
cycle = 0
wait = 0
wait_buffer = 0
for statement in program:
    already = False
    if statement.startswith('noop'):
        cycle += 1
        if (cycle % 40) in sprite_pos:
            pixels.append('#')
        else:
            pixels.append('.')
    elif statement.startswith('addx'):
        command, argument = statement.split()
        argument = int(argument)
        wait = 2
        wait_buffer = argument
        while wait > 0:
            cycle += 1
            wait -= 1
            if (cycle % 40) in sprite_pos:
                pixels.append('#')
            else:
                pixels.append('.')
            if cycle > 0 and ((cycle - 20) % 40 == 0 or cycle == 20):
                signal_strengths.append(cycle * x)
                already = True
        x += wait_buffer
        wait_buffer = 0
        sprite_pos = [x, x + 1, x + 2]
    if not(already) and (cycle > 0 and ((cycle - 20) % 40 == 0 or cycle == 20)):
        signal_strengths.append(cycle * x)
        if (cycle % 40) in sprite_pos:
            pixels.append('#')
        else:
            pixels.append('.')

print(sum(signal_strengths))

for i, c in enumerate(pixels):
    if i > 0 and (i % 40) == 0:
        print()
    print(c, end='')
# prints PZGPKPEB