FILENAME = '4.in'


def parse_allocation(l):
    return tuple([int(x) for x in l.split('-')])


def fully_contains(l, r):

    def fully_contains_directed(l, r):
        s1, e1 = parse_allocation(l)
        s2, e2 = parse_allocation(r)
        return s1 <= s2 and e1 >= e2

    return fully_contains_directed(l, r) or fully_contains_directed(r, l)


def overlaps(l, r):

    def overlaps_directed(l, r):
        s1, e1 = parse_allocation(l)
        s2, e2 = parse_allocation(r)
        return (s1 <= s2 and e1 >= s2 and e1 <= e2) or (s1 >= s2 and s1 <= e2 and e1 >= e2) or fully_contains(l, r)

    return overlaps_directed(l, r) or overlaps_directed(r, l)


def redundancy(assignments, predicate):
    redundant_assignments = 0
    for l, r in assignments:
        if predicate(l, r):
            redundant_assignments += 1
    return redundant_assignments


assignments = [tuple(l.strip().split(',')) for l in open(FILENAME, 'r').readlines()]

print(redundancy(assignments, fully_contains))
print(redundancy(assignments, overlaps))