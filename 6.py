FILENAME = '6.in'


def find_marker(sequence, window_size):
    marker = (None, None)
    for i in range(0, len(sequence) - window_size + 1):
        window = sequence[i:i+window_size]
        if all(window.count(c) == 1 for c in window):
            marker = (i + window_size, sequence[i:i+window_size])
            break
    return marker


sequence = [l.strip() for l in open(FILENAME, 'r').readlines()][0]

print(find_marker(sequence, 4))
print(find_marker(sequence, 14))