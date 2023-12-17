import heapq


def ll():
    try:
        return input().strip()
    except:
        return None


g = []
while (l := ll()) is not None:
    if l:
        g.append([int(x) for x in l])
        continue

q = [(0, 0, 0, "d"), (0, 0, 0, "r")]
visited = set()
while q:
    c, x, y, d = heapq.heappop(q)
    if (x, y, d) in visited:
        continue
    visited.add((x, y, d))

    if y == len(g) - 1 and x == len(g[y]) - 1:
        print(c)
        break

    for i in range(3):
        if d == "r":
            x += 1
        elif d == "l":
            x -= 1
        elif d == "u":
            y -= 1
        elif d == "d":
            y += 1

        if x < 0 or y < 0 or y >= len(g) or x >= len(g[y]):
            break

        c += g[y][x]
        for dir in "rl" if d in "ud" else "ud":
            heapq.heappush(q, (c, x, y, dir))
