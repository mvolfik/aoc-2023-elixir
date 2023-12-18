from collections import defaultdict


def ll():
    try:
        return input().strip()
    except:
        return None


g = defaultdict(lambda: ".")

points = [(0, 0)]
x, y = 0, 0
line_len = 1
while (l := ll()) is not None:
    if not l:
        continue
    a, b, c = l.split(" ")
    b = int(c[2:-2], 16)
    a = "RDLU"[int(c[-2])]
    if a == "R":
        x += b
    elif a == "L":
        x -= b
    elif a == "U":
        y -= b
    elif a == "D":
        y += b
    line_len += b / 2

    points.append((x, y))

assert points[0] == points[-1]

a = 0
for i in range(len(points) - 1):
    a += points[i][0] * points[i + 1][1] - points[i + 1][0] * points[i][1]
print(line_len, abs(a) / 2, line_len + (abs(a) / 2))
