# borrowed a few things here and there from https://www.youtube.com/watch?v=bLMj50cpOug&t=1586s
# tough AoC puzzle today, but refreshed a lot and also learned a couple of new things. the
# aforementioned video was really heplful.

from collections import deque


FILENAME = '16.in'
CACHE_DFS = {}


def parse_flow_rate(line):
    return int(line.split(';')[0].split('=')[1])


def parse_valve(line):
    return line.split(' ')[1].strip()


def parse_adjacent_valves(line):
    return [v.strip() for v in line.split(' to ')[1].split(' ', 1)[1].split(', ')]


def parse(filename):
    valves = {}
    tunnels = {}
    lines = [l.strip() for l in open(filename, 'r').readlines()]
    for l in lines:
        flow = parse_flow_rate(l)
        valve = parse_valve(l)
        adjacent_valves = parse_adjacent_valves(l)
        valves[valve] = flow
        tunnels[valve] = adjacent_valves
    return valves, tunnels


def compute_distances(valves, tunnels):
    distances = {}
    valves_with_possible_flow = []
    for valve in valves:
        if valve != 'AA' and not valves[valve]:
            continue
        if valve != 'AA':
            valves_with_possible_flow.append(valve)

        distances[valve] = { valve: 0, 'AA': 0 }
        visited = { valve }

        # starting with 0 for the distance and the current
        # valve for the starting point
        queue = deque()
        queue.append((0, valve))

        while queue:
            distance, position = queue.popleft()
            for neighbour in tunnels[position]:
                if neighbour in visited:
                    continue
                visited.add(neighbour)
                # we can omit the conditional here, this is just
                # a slight optimization as we can skip those nodes
                # that cannot contribute to the overall flow
                # (flow rate = 0)
                if valves[neighbour]:
                    distances[valve][neighbour] = distance + 1
                queue.append((distance + 1, neighbour))

        del distances[valve][valve]

        if valve != 'AA':
            del distances[valve]['AA']
    return distances, valves_with_possible_flow


def compute_index(non_empty):
    index = {}
    for i, element in enumerate(non_empty):
        index[element] = i
    return index


# for some reason, Python's LRU cache performans terribly.
# so instead, we roll our own memoization strategy
# the algorithm is a basic DFS that goes over all possible
# states in order to compute the max flow possible with
# respect to the time remaining to open a valve / walk to
# another valve
# the state of open/closed valves is represented using a
# bitmask (which relies on a computed index of valves in
# order to know which bit has to be flipped once a valve
# goes from closed to open state)
def dfs(time, valve, bitmask):
    if (time, valve, bitmask) in CACHE_DFS:
        return CACHE_DFS[(time, valve, bitmask)]
    max_flow = 0
    for neighbour in distances[valve]:
        bit = 1 << index[neighbour]
        # the valve is already open, so let's skip it
        if bitmask & bit:
            continue
        remaining_time = time - distances[valve][neighbour] - 1 # walk and open
        if remaining_time <= 0:
            # if there is no time remaining, then there is no point in opening
            # the valve at all, so we just skip it
            continue
        max_flow = max(max_flow, dfs(remaining_time, neighbour, bitmask | bit) + valves[neighbour] * remaining_time)
    CACHE_DFS[(time, valve, bitmask)] = max_flow
    return max_flow


valves, tunnels = parse(FILENAME)
distances, valves_with_possible_flow = compute_distances(valves, tunnels)
index = compute_index(valves_with_possible_flow)
print(dfs(30, 'AA', 0))
b = (1 << len(valves_with_possible_flow)) - 1
max_flow_with_helper = 0
for i in range(b + 1):
    max_flow_with_helper = max(max_flow_with_helper, dfs(26, 'AA', i) + dfs(26, 'AA', b ^ i))
print(max_flow_with_helper)