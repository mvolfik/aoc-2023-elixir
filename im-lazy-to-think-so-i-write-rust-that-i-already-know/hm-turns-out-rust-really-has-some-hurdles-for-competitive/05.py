see = [int(x) for x in input().split(": ")[1].split()]
see = [(see[x], see[x + 1]) for x in range(0, len(see), 2)]


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
        if current is not None:
            current.sort()
        current = []
        s = l.split()[0].split("-")
        maps[s[0]] = (s[2], current)
        continue

    a, b, c = map(int, l.split())
    current.append((b, a, c))


def process(k, start1, len1):
    print(k, start1, len1)
    if k == "location":
        return start1
    (next, m) = maps[k]
    low = 999999999999
    for start, target, len in m:
        offset = start1 - start
        if offset < 0:
            seg_len = min(len1, -offset)
            print("copy seg", start1, seg_len)
            low = min(low, process(next, start1, seg_len))
            start1 += seg_len
            len1 -= seg_len
            if len1 == 0:
                break

        offset = start1 - start
        assert offset >= 0
        if offset < len:
            seg_len = min(len1, len - offset)
            low = min(low, process(next, target + offset, seg_len))
            start1 += seg_len
            len1 -= seg_len
            if len1 == 0:
                break

    if len1 > 0:
        low = min(low, process(next, start1, len1))

    return low


low = 999999999999
for s, l in see:
    low = min(low, process("seed", s, l))

print(low)
