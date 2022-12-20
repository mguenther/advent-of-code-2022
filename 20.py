FILENAME = '20.in'


def get(i, n):
    j = 0
    for k in range(len(n)):
        if n[k][1] == 0:
            j = k
            break
    return n[(i + j) % len(n)][1]


def solve(rounds = 1, multiplier = 1):
    numbers = [(i, int(l.strip()) * multiplier) for i, l in enumerate(open(FILENAME, 'r').readlines())]
    length = len(numbers)
    for _ in range(rounds):
        for i in range(length):
            indexed_element, original_index = None, None
            for k in range(length):
                if numbers[k][0] == i:
                    indexed_element = numbers[k]
                    original_index = k
                    break
            # if the value is 0, we're doing nothing
            # (this is just for the sake cleanliness, the algorithm
            # works correctly without that step)
            if indexed_element[1] == 0:
                continue
            # otherwise, we'll determine the new index position,
            # remove the element from the old position and insert
            # it into the list at the new position
            j = (k + indexed_element[1]) % (length - 1)
            del numbers[original_index]
            numbers.insert(j, indexed_element)
    return get(1000, numbers) + get(2000, numbers) + get(3000, numbers)


print(solve())
print(solve(rounds = 10, multiplier = 811589153))