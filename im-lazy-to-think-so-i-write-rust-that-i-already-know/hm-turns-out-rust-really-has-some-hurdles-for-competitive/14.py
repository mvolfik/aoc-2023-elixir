from collections import defaultdict


def ll():
    try:
        return input().strip()
    except:
        return None


def tiltu(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] != "O":
                continue
            y1 = y - 1
            while y1 >= 0 and grid[y1][x] == ".":
                grid[y1][x] = "O"
                grid[y1 + 1][x] = "."
                y1 -= 1


def tiltd(grid):
    for y in reversed(range(len(grid))):
        for x in range(len(grid[0])):
            if grid[y][x] != "O":
                continue
            y1 = y + 1
            while y1 < len(grid) and grid[y1][x] == ".":
                grid[y1][x] = "O"
                grid[y1 - 1][x] = "."
                y1 += 1


def tiltl(grid):
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            if grid[y][x] != "O":
                continue
            x1 = x - 1
            while x1 >= 0 and grid[y][x1] == ".":
                grid[y][x1] = "O"
                grid[y][x1 + 1] = "."
                x1 -= 1


def tiltr(grid):
    for x in reversed(range(len(grid[0]))):
        for y in range(len(grid)):
            if grid[y][x] != "O":
                continue
            x1 = x + 1
            while x1 < len(grid[0]) and grid[y][x1] == ".":
                grid[y][x1] = "O"
                grid[y][x1 - 1] = "."
                x1 += 1


g = []
while (l := ll()) is not None:
    if l:
        g.append(list(l))
        continue

mapping = defaultdict(list)

aaaa = 20
aaaa = 1000000000
for i in range(aaaa):
    print(i)
    tiltu(g)
    tiltl(g)
    tiltd(g)
    tiltr(g)
    hash = "\n".join("".join(x) for x in g)
    print(hash)
    print()
    mapping[hash].append(i)
    if len(mapping[hash]) == 2:
        print("seen after", i, mapping[hash])
        break

cycle = mapping[hash]
cyclen = cycle[1] - cycle[0]

remaining = aaaa - cycle[1]
mults = remaining // cyclen
print(cyclen, mults, remaining)
for i in range(mults * cyclen + cycle[1] + 1, aaaa):
    print(i)
    tiltu(g)
    tiltl(g)
    tiltd(g)
    tiltr(g)


s = 0
for i in range(len(g)):
    for j in range(len(g[0])):
        if g[i][j] == "O":
            s += len(g) - i
print(s)
