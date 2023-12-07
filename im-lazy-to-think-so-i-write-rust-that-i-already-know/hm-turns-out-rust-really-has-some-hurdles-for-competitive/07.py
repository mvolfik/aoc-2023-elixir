from collections import defaultdict


def ll():
    try:
        return input().strip()
    except:
        return None


cards = "AKQT98765432J"

hands = []
while (l := ll()) is not None:
    if not l:
        continue

    x, bid = l.split()
    bid = int(bid)

    d = defaultdict(int)
    for c in x:
        if c == "J":
            continue
        d[c] += 1

    counts = sorted(d.items(), key=lambda x: (-x[1], cards.index(x[0])))

    if len(counts) == 0:
        counts.append(("J", 0))
    for c in x:
        if c == "J":
            counts[0] = (counts[0][0], counts[0][1] + 1)
    hands.append((bid, counts, x))


def getkey(hand):
    _, counts, x = hand
    x = [cards.index(c) for c in x]
    print(x)
    if counts[0][1] == 5:
        return (0, x)
    if counts[0][1] == 4:
        return (1, x)
    if counts[0][1] == 3 and counts[1][1] == 2:
        return (2, x)
    if counts[0][1] == 3:
        return (3, x)
    if counts[0][1] == 2 and counts[1][1] == 2:
        return (4, x)
    if counts[0][1] == 2:
        return (5, x)
    return (6, x)


hands.sort(key=getkey)
hands.reverse()
s = 0
for i in range(len(hands)):
    s += hands[i][0] * (i + 1)

print(s)
