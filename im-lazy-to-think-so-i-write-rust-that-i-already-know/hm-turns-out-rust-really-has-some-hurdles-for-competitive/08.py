import math


def ll():
    try:
        return input().strip()
    except:
        return None


seq = input()

input()

rules = {}
while (l := ll()) is not None:
    if not l:
        continue

    x, y = l.split(" = ")
    rules[x] = tuple(y[1:-1].split(", "))

nodes = [x for x in rules if x[-1] == "A"]
ii = 1

for n in nodes:
    i = 0
    while True:
        if n[-1] == "Z":
            break
        y = rules[n]
        if seq[i % len(seq)] == "R":
            n = y[1]
        else:
            n = y[0]
        i += 1
    ii = math.lcm(ii, i)
print(ii)
