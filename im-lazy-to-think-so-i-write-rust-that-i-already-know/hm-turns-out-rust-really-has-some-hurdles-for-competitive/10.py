def ll():
    try:
        return input().strip()
    except:
        return None


grid = []
while (l := ll()) is not None:
    if not l:
        continue
    x = []
    x.append(l[0])
    for i in range(1, len(l)):
        x.append(" ")
        x.append(l[i])
    grid.append(x)
    grid.append([" "] * len(x))
grid.pop()
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

while True:
    c = grid[y][x]
    print(f"{x}, {y} {f} {c}")

    grid[y][x] = "#"
    if f == "bot" and c == "|":
        y -= 1
        grid[y][x] = "#"
        y -= 1
    elif f == "top" and c == "|":
        y += 1
        grid[y][x] = "#"
        y += 1
    elif f == "left" and c == "-":
        x += 1
        grid[y][x] = "#"
        x += 1
    elif f == "right" and c == "-":
        x -= 1
        grid[y][x] = "#"
        x -= 1

    elif f == "bot" and c == "F":
        x += 1
        grid[y][x] = "#"
        x += 1
        f = "left"
    elif f == "right" and c == "F":
        y += 1
        grid[y][x] = "#"
        y += 1
        f = "top"

    elif f == "top" and c == "L":
        x += 1
        grid[y][x] = "#"
        x += 1
        f = "left"
    elif f == "right" and c == "L":
        y -= 1
        grid[y][x] = "#"
        y -= 1
        f = "bot"

    elif f == "left" and c == "J":
        y -= 1
        grid[y][x] = "#"
        y -= 1
        f = "bot"
    elif f == "top" and c == "J":
        x -= 1
        grid[y][x] = "#"
        x -= 1
        f = "right"

    elif f == "left" and c == "7":
        y += 1
        grid[y][x] = "#"
        y += 1
        f = "top"
    elif f == "bot" and c == "7":
        x -= 1
        grid[y][x] = "#"
        x -= 1
        f = "right"
    else:
        raise Exception(f"Unknown char {c} at {x}, {y} from {f}")

    if (x, y) == (sx, sy):
        break

q = set()
q.add((0, 0))

while len(q) > 0:
    x, y = q.pop()
    if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
        continue

    if grid[y][x] in "#*":
        continue

    grid[y][x] = "*"
    q.add((x + 1, y))
    q.add((x - 1, y))
    q.add((x, y + 1))
    q.add((x, y - 1))

for l in grid:
    print("".join(l))

n = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] not in "#* ":
            n += 1
print(n)
