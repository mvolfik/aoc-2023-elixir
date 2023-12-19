from collections import defaultdict
from functools import reduce


def ll():
    try:
        return input().strip()
    except:
        return None


rules = {}
while (l := ll()) is not None:
    if not l:
        break

    a, b = l[:-1].split("{")
    rules[a] = [
        (x[0], x[1], *x[2:].split(":")) if ":" in x else x for x in b.split(",")
    ]
print(rules)


def process(state, ranges):
    if state == "R":
        return 0
    if state == "A":
        return reduce(lambda a, b: a * b, (r[1] - r[0] + 1 for r in ranges), 1)

    s = 0
    ranges = ranges.copy()
    for r in rules[state]:
        if isinstance(r, str):
            s += process(r, ranges)
            continue

        (letter, compop, val, next) = r
        val = int(val)
        rangeIndex = "xmas".index(letter)
        low, hi = ranges[rangeIndex]

        subrange = None
        if compop == "<":
            subrange = (low, val - 1)
            ranges[rangeIndex] = (val, hi)
        elif compop == ">":
            subrange = (val + 1, hi)
            ranges[rangeIndex] = (low, val)
        else:
            raise Exception("Unknown compop")
        s += process(next, ranges[:rangeIndex] + [subrange] + ranges[rangeIndex + 1 :])
    return s


print(process("in", [(1, 4000), (1, 4000), (1, 4000), (1, 4000)]))
