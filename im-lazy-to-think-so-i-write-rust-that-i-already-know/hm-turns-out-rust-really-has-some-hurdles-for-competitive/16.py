def ll():
    try:
        return input().strip()
    except:
        return None


g = []
while (l := ll()) is not None:
    if l:
        g.append(l)
        continue

starts = []
for i in range(len(g)):
    starts.append((0, i, "r"))
    starts.append((len(g[i]) - 1, i, "l"))

for i in range(len(g[0])):
    starts.append((i, 0, "d"))
    starts.append((i, len(g) - 1, "u"))

m = 0
aaaa = None
for start in starts:
    known = set()

    next = set()
    next.add(start)

    modified = [list(x) for x in g]

    while next:
        it = next.pop()
        x, y, d = it
        if x < 0 or y < 0 or y >= len(g) or x >= len(g[y]):
            continue

        if it in known:
            continue
        known.add(it)
        modified[y][x] = "#"
        # print(it)
        # print("\n".join("".join(x) for x in modified))

        c = g[y][x]
        if d == "r":
            if c in ".-":
                next.add((x + 1, y, d))
            elif c == "|":
                next.add((x, y - 1, "u"))
                next.add((x, y + 1, "d"))
            elif c == "/":
                next.add((x, y - 1, "u"))
            elif c == "\\":
                next.add((x, y + 1, "d"))
        if d == "l":
            if c in ".-":
                next.add((x - 1, y, d))
            elif c == "|":
                next.add((x, y - 1, "u"))
                next.add((x, y + 1, "d"))
            elif c == "/":
                next.add((x, y + 1, "d"))
            elif c == "\\":
                next.add((x, y - 1, "u"))
        if d == "u":
            if c in ".|":
                next.add((x, y - 1, d))
            elif c == "-":
                next.add((x - 1, y, "l"))
                next.add((x + 1, y, "r"))
            elif c == "/":
                next.add((x + 1, y, "r"))
            elif c == "\\":
                next.add((x - 1, y, "l"))
        if d == "d":
            if c in ".|":
                next.add((x, y + 1, d))
            elif c == "-":
                next.add((x - 1, y, "l"))
                next.add((x + 1, y, "r"))
            elif c == "/":
                next.add((x - 1, y, "l"))
            elif c == "\\":
                next.add((x + 1, y, "r"))
    size = len(set(x[:2] for x in known))
    if size > m:
        m = size
        aaaa = start
print(m, aaaa)
