from collections import defaultdict


FILENAME = '7.in'
DEBUG = False
TOTAL_DISK_SPACE = 70000000
REQUIRED_UNUSED_DISK_SPACE = 30000000


def is_command(line):
    return line.startswith('$')


def is_directory(line):
    return line.startswith('dir')


def on_command(line, current_directory):
    tokens = line.split(' ')
    if tokens[1] == 'cd':
        # change directory
        target = tokens[2]
        if target == '..':
            current_directory.pop()
        elif target == '/':
            current_directory = ['']
        else:
            current_directory.append(target)
        if DEBUG:
            print('Changed directory to:', '/'.join(current_directory))


def on_directory(line):
    if DEBUG:
        tokens = line.split(' ')
        print('Discovered directory:', tokens[1])


def on_file(line, current_directory, sizes_per_directory):
    tokens = line.split(' ')
    filesize = int(tokens[0])
    filename = tokens[1]
    if DEBUG:
        print('Discovered file', filename, 'with size', filesize)
    for i in range(len(current_directory)):
        subpath = '/'.join(current_directory[0:i+1])
        sizes_per_directory[subpath] += filesize


def parse(filename):
    lines = [l.strip() for l in open(filename, 'r').readlines()]
    current_directory = ['']
    sizes_per_directory = defaultdict(int)

    for line in lines:
        if is_command(line):
            on_command(line, current_directory)
        elif is_directory(line):
            on_directory(line)
        else:
            on_file(line, current_directory, sizes_per_directory)

    return sizes_per_directory


def solve_first_part(sizes_per_directory):
    total = 0
    for _, size in sizes_per_directory.items():
        if size < 100000:
            total += size
    return total


def solve_second_part(sizes_per_directory):
    unused_space = TOTAL_DISK_SPACE - sizes_per_directory['']
    free_up_space = REQUIRED_UNUSED_DISK_SPACE - unused_space
    if DEBUG:
        print('Unused disk space is', unused_space)
        print('Required to free up', free_up_space)
    qualifies_for_deletion = []
    for directory, size in sizes_per_directory.items():
        if size >= free_up_space:
            qualifies_for_deletion.append((directory, size))
    if DEBUG:
        print(qualifies_for_deletion)
        print(min(qualifies_for_deletion, key = lambda p: p[1]))
    return min(qualifies_for_deletion, key = lambda p: p[1])[1]


sizes_per_directory = parse(FILENAME)

print(solve_first_part(sizes_per_directory))
print(solve_second_part(sizes_per_directory))
