from collections import defaultdict


def ll():
    try:
        return input().strip()
    except:
        return None


boxes = [[] for _ in range(256)]
while (l := ll()) is not None:
    if not l:
        continue

    for x in l.split(","):
        if not x:
            continue

        n = None
        if x[-1] == "-":
            label = x[:-1]
        else:
            label, n = x.split("=")

        v = 0
        for c in label:
            v = (v + ord(c)) * 17 % 256

        box = boxes[v]
        if n is None:
            for i in range(len(box)):
                if box[i][0] == label:
                    boxes[v] = box[:i] + box[i + 1 :]
                    break
        else:
            for i in range(len(box)):
                if box[i][0] == label:
                    box[i] = (label, int(n))
                    break
            else:
                box.append((label, int(n)))
        print(x)
        print(boxes)

s = 0
for i in range(len(boxes)):
    for j in range(len(boxes[i])):
        s += boxes[i][j][1] * (i + 1) * (j + 1)
print(s)
