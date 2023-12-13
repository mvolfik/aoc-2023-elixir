def ll():
    try:
        return input().strip()
    except:
        return None


def f(grid):
    print("\n".join("".join(x) for x in grid))
    for i in range(1, len(grid)):
        print()
        print(i)
        ok = True
        for j in range(min(i, len(grid) - i)):
            y1 = i + j
            y2 = i - j - 1
            print(y1, y2)
            for x in range(len(grid[0])):
                print("comparing", y1, y2, x)
                if grid[y1][x] != grid[y2][x]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            return i


s = 0
g = []
while (l := ll()) is not None:
    if l:
        g.append(l)
        continue
    g2 = g
    g = []
    horizontal = f(list(zip(*g2)))
    if horizontal is not None:
        s += horizontal
        continue
    vertical = f(g2)
    if vertical is not None:
        s += vertical * 100
        continue

    raise Exception("No solution")

g2 = g
horizontal = f(list(zip(*g2)))
if horizontal is not None:
    s += horizontal
else:
    vertical = f(g2)
    if vertical is not None:
        s += vertical * 100
    else:
        raise Exception("No solution")

print(s)
