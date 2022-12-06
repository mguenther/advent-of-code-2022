FILENAME = '6.in'


def find_marker(sequence, window_size):
    for i in range(0, len(sequence) - window_size + 1):
        window = sequence[i:i+window_size]
        if all(window.count(c) == 1 for c in window):
            return (i + window_size, sequence[i:i+window_size])
    return (None, None)


sequence = [l.strip() for l in open(FILENAME, 'r').readlines()][0]

print(find_marker(sequence, 4))
print(find_marker(sequence, 14))