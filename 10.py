FILENAME = '10.in'


program = [l.strip() for l in open(FILENAME, 'r').readlines()]
signal_strengths = []
pixels = []
sprite_pos = [1, 2, 3]
x = 1
cycle = 1
wait = 0
wait_buffer = 0
for statement in program:
    already = False
    if statement.startswith('noop'):
        if (cycle % 40) in sprite_pos:
            pixels.append('#')
        else:
            pixels.append('.')
        cycle += 1
        print(cycle, x, sprite_pos)
    elif statement.startswith('addx'):
        command, argument = statement.split()
        argument = int(argument)
        wait = 2
        wait_buffer = argument
        while wait > 0:
            if (cycle % 40) in sprite_pos:
                pixels.append('#')
            else:
                pixels.append('.')
            cycle += 1
            wait -= 1
            print(cycle, x, sprite_pos)
            if cycle > 0 and ((cycle - 20) % 40 == 0 or cycle == 20):
                print('cycle at', cycle, 'value of x:', x)
                signal_strengths.append(cycle * x)
                already = True
        x += wait_buffer
        wait_buffer = 0
        sprite_pos = [x, x + 1, x + 2]      
    if not(already) and (cycle > 0 and ((cycle - 20) % 40 == 0 or cycle == 20)):
        print('cycle at', cycle, 'value of x:', x)
        signal_strengths.append(cycle * x)
        if (cycle % 40) in sprite_pos:
            pixels.append('#')
        else:
            pixels.append('.')

print(cycle, x)
print(signal_strengths)
print(sum(signal_strengths))

for i, c in enumerate(pixels):
    if i > 1 and (i % 40) == 0:
        print()
    print(c, end='')
# prints PZGPKPEB