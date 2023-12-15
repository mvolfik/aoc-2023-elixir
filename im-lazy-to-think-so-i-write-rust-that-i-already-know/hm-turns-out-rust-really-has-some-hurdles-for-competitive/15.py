from collections import defaultdict


def ll():
    try:
        return input().strip()
    except:
        return None


s = 0
while (l := ll()) is not None:
    if not l:
        continue

    for x in l.split(","):
        if not x:
            continue

        v = 0
        for c in x:
            v = (v + ord(c)) * 17 % 256
        s += v
        print(v)
print(s)
