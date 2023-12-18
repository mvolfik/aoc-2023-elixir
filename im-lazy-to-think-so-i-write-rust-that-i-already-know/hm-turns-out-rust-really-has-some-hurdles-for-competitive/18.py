from collections import defaultdict


def ll():
    try:
        return input().strip()
    except:
        return None


g = defaultdict(lambda: ".")

x, y = 0, 0
g[(x, y)] = "#"
while (l := ll()) is not None:
    if not l:
        continue
    a, b, c = l.split(" ")
    for i in range(int(b)):
        if a == "R":
            x += 1
        elif a == "L":
            x -= 1
        elif a == "U":
            y -= 1
        elif a == "D":
            y += 1

        g[(x, y)] = "#"

minx = min(x for x, y in g.keys())
maxx = max(x for x, y in g.keys())
miny = min(y for x, y in g.keys())
maxy = max(y for x, y in g.keys())

for y in range(miny, maxy + 1):
    for x in range(minx, maxx + 1):
        print(g[(x, y)], end="")
    print()

q = set()
q.add(
    (
        minx
        + len(
            "......................................................................................................................................#...#...#......."
        ),
        miny + 10,
    )
)

while q:
    x, y = q.pop()
    if x < minx or x > maxx or y < miny or y > maxy:
        raise Exception(f"Out of bounds {x}, {y}")
    g[(x, y)] = "#"

    for item in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if g[item] == "#":
            continue
        g[item] = "#"
        q.add(item)

print(sum(1 for x, y in g.keys() if g[(x, y)] == "#"))


for y in range(miny, maxy + 1):
    for x in range(minx, maxx + 1):
        print(g[(x, y)], end="")
    print()
