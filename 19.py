from math import ceil
from copy import deepcopy

import re


FILENAME = '19.in'
# we'll map resource types to indices so that we can easily access
# them by index in a tuple or list
TYPE_INDEX = {
    'ore': 0,
    'clay': 1,
    'obsidian': 2
}


def empty_blueprint():
    # we'll use a simple dict that stores both all of the requirements
    # that this blueprint comprises, as well as all the required
    # information to reduce the search space by applying heuristics
    return {
        'requirements': [],
        # this is actually an optimization technique I 'borrowed' from
        # Jonathan Paulson. the gist of it is that we don't need any more
        # robots that produce a given resource type, if produce enough
        # of that resource type per step to build *any* of the robots
        # in our blueprint
        # this drastically limits the search space, especially for part
        # two of this puzzle, so CPython has a chance to exhaust the
        # search space in a reasonable amount of time
        'maximum_spend_per_type': {
            0: 0,
            1: 0,
            2: 0
        }
    }


def parse(filename):
    lines = [l.strip() for l in open(filename, 'r').readlines()]
    blueprints = []
    for line in lines:
        blueprint = empty_blueprint()
        for segment in line.split(': ')[1].split('. '):
            requirements = []
            for amount, type in re.findall(r"(\d+) (\w+)", segment):
                amount = int(amount)
                type = TYPE_INDEX[type]
                requirements.append((amount, type))
                blueprint['maximum_spend_per_type'][type] = max(blueprint['maximum_spend_per_type'][type], amount)
            blueprint['requirements'].append(requirements)
        blueprints.append(blueprint)
    return blueprints


def to_cache_key(remaining_time, active_bots, amount):
    return tuple([remaining_time, *active_bots, *amount])


def compute_gain(blueprint, cache, remaining_time, active_bots, amount):

    if remaining_time == 0:
        return amount[3]

    cache_key = to_cache_key(remaining_time, active_bots, amount)

    if cache_key in cache:
        return cache[cache_key]

    # do nothing, just accumulate geodes with the set of active
    # bots that we currently have; of course, we only care for
    # the production of new geodes that *this* step contributes
    # to the value
    value = amount[3] + active_bots[3] * remaining_time
    # otherwise, we'll check how long it would take to produce
    # an additional bot of each type (considering some time to wait
    # to accumulate the necessary resources) and see if this yields
    # a better overall gain
    for bot_type, requirements in enumerate(blueprint['requirements']):
        # we do not need to build new bots of the given type if
        # we are already able to construct one of those bots within
        # a single step (as we can only produce *one* robot per step)
        if bot_type != 3 and active_bots[bot_type] >= blueprint['maximum_spend_per_type'][bot_type]:
            continue
        wait_steps = 0
        for required_amount, required_type in requirements:
            # if we do not have any bots that can contribute to
            # the required amount of the required type, than we
            # do not need to bother at all
            if active_bots[required_type] == 0:
                break
            steps_to_produce_bot_of_type = int(ceil((required_amount - amount[required_type]) / active_bots[required_type]))
            wait_steps = max(wait_steps, steps_to_produce_bot_of_type)
        else:
            updated_remaining_time = remaining_time - wait_steps - 1
            # we can skip the next state if the updated remaining
            # time is exhausted, as the freshly produced bot will
            # get the chance to gather resources
            if updated_remaining_time <= 0:
                continue
            active_bots_ = deepcopy(active_bots)
            updated_amount = [amount_of_type + bot_of_type * (wait_steps + 1) for amount_of_type, bot_of_type in zip(amount, active_bots)]
            for required_amount, required_type in requirements:
                updated_amount[required_type] -= required_amount
            active_bots_[bot_type] += 1
            for i in range(3):
                updated_amount[i] = min(updated_amount[i], active_bots[i] * updated_remaining_time)
            value = max(value, compute_gain(blueprint, cache, updated_remaining_time, active_bots_, updated_amount))
    cache[cache_key] = value
    return value


def solve_part_one(filename):
    blueprints = parse(filename)
    total = 0
    for i, blueprint in enumerate(blueprints):
        gain = compute_gain(blueprint, {}, 24, [1, 0, 0, 0], [0, 0, 0, 0])
        total += (i + 1) * gain
    return total


def solve_part_two(filename):
    blueprints = parse(filename)
    total = 1
    for blueprint in blueprints[:3]:
        gain = compute_gain(blueprint, {}, 32, [1, 0, 0, 0], [0, 0, 0, 0])
        total *= gain
    return total


print(solve_part_one(FILENAME))
print(solve_part_two(FILENAME))