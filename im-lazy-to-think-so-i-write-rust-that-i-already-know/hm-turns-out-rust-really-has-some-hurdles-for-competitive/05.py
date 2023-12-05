see = [int(x) for x in input().split(": ")[1].split()]


def ll():
    try:
        return input().strip()
    except:
        return None


maps = {}
current = None
while (l := ll()) is not None:
    if not l:
        continue

    if l.endswith("map:"):
        current = {}
        s = l.split()[0].split("-")
        maps[s[0]] = (s[2], current)
        continue

    a, b, c = map(int, l.split())
    current[b] = (a, c)

low = 9999999999999
for s in see:
    k = "seed"
    while k != "location":
        print(k, s)
        k, m = maps[k]
        for start,(target,len) in m.items():
            offset = s - start
            if offset >= 0 and offset < len:
                s = target + offset
                break
        else:
            pass
            # raise Exception("no path")

    low = min(low, s)
print(low)