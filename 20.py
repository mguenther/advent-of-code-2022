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
            t = None
            ii = None
            for k in range(length):
                if numbers[k][0] == i:
                    t = numbers[k]
                    ii = k
                    break

            # if the value is 0, we're doing nothing
            if t[1] == 0:
                continue

            # otherwise, we'll determine the new index position
            j = (k + t[1]) % (length - 1)
            del numbers[ii]
            numbers.insert(j, t)

    a = get(1000, numbers)
    b = get(2000, numbers)
    c = get(3000, numbers)

    return get(1000, numbers) + get(2000, numbers) + get(3000, numbers)


print(solve())
print(solve(rounds = 10, multiplier = 811589153))