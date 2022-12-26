import math


FILENAME = '25.in'
MAPPING_TO_DECIMAL = {
    '2': 2,
    '1': 1,
    '0': 0,
    '-': -1,
    '=': -2
}
# account for balanced ternary to the base of 5
MAPPING_TO_SNAFU = {
    0: ' ',
    1: ' ',
    2: ' ',
    3: '=',
    4: '-'
}


def to_decimal(snafu_number):
    l = len(snafu_number)
    decimal_number = 0
    for i, snafu_literal in enumerate(snafu_number):
        j = l - i - 1
        m = MAPPING_TO_DECIMAL[snafu_literal]
        decimal_number += m * math.pow(5, j)
    return int(decimal_number)


def to_snafu(decimal_number):
    snafu_number = ''
    while decimal_number:
        rem = decimal_number % 5
        decimal_number //= 5
        if rem <= 2:
            snafu_number = str(rem) + snafu_number
        else:
            snafu_number = MAPPING_TO_SNAFU[rem] + snafu_number
            decimal_number += 1
    return snafu_number


snafu_numbers = [l.strip() for l in open(FILENAME, 'r').readlines()]
total = 0
for snafu_number in snafu_numbers:
    total += to_decimal(snafu_number)
print(total)
print(to_snafu(total))