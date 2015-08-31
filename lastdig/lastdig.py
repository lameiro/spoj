lookup_table = {
    0: ([0], 1),
    1: ([1], 0),
    2: ([2, 4, 8, 6], 1),
    3: ([1, 3, 9, 7], 0),
    4: ([4, 6], 1),
    5: ([5], 1),
    6: ([6], 1),
    7: ([1, 7, 9, 3], 0),
    8: ([8, 4, 2, 6], 1),
    9: ([1, 9], 0),
}

def solve(base, exponent):
    base %= 10
    period, offset = lookup_table[base]

    if exponent < offset:
        return 1

    result = period[exponent % len(period) - offset]

    return result

def main():
    nr_of_cases = int(raw_input())

    for i in xrange(nr_of_cases):
        base, exponent = map(int, raw_input().split())
        print solve(base, exponent)

main()
