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

X = 1000000-1
coloffset = {}
offset = 0
for i in range(len(grid)):
    coloffset[i] = i+offset
    l = grid[i]
    if "#" not in l:
        offset += X
print(coloffset)
n = [[] for _ in grid[0]]
for l in grid:
    for i in range(len(l)):
        n[i].append(l[i])
grid = n

rowoffset = {}
offset = 0
for i in range(len(grid)):
    rowoffset[i] = i+offset
    l = grid[i]
    if "#" not in l:
        offset += X

n = [[] for _ in grid[0]]
for l in grid:
    for i in range(len(l)):
        n[i].append(l[i])
grid = n


galaxies = []

for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == "#":
            print(x, y, coloffset[y], rowoffset[x])
            galaxies.append((coloffset[y], rowoffset[x]))
print(galaxies)
s = 0
for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        x1, y1 = galaxies[i]
        x2, y2 = galaxies[j]
        s += abs(x1 - x2) + abs(y1 - y2)
print(s)