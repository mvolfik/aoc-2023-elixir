def ll():
    try:
        return input().strip()
    except:
        return None


grid = []
while (l := ll()) is not None:
    if not l:
        continue
    grid.append(list(l))

sx, sy = 0, 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == "S":
            sx, sy = x, y
            break
    else:
        continue
    break

x, y = sx, sy
grid[y][x] = "|"
f = "bot"
n = 0
while True:
    c = grid[y][x]
    print(f"{x}, {y} {f} {c}")
    if f == "bot" and c == "|":
        y -= 1
    elif f == "top" and c == "|":
        y += 1
    elif f == "left" and c == "-":
        x += 1
    elif f == "right" and c == "-":
        x -= 1

    elif f == "bot" and c == "F":
        x += 1
        f = "left"
    elif f == "right" and c == "F":
        y += 1
        f = "top"

    elif f == "top" and c == "L":
        x += 1
        f = "left"
    elif f == "right" and c == "L":
        y -= 1
        f = "bot"

    elif f == "left" and c == "J":
        y -= 1
        f = "bot"
    elif f == "top" and c == "J":
        x -= 1
        f = "right"

    elif f == "left" and c == "7":
        y += 1
        f = "top"
    elif f == "bot" and c == "7":
        x -= 1
        f = "right"
    else:
        raise Exception(f"Unknown char {c} at {x}, {y} from {f}")

    n += 1
    if (x, y) == (sx, sy):
        break

print(n / 2)
