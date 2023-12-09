import math


def ll():
    try:
        return input().strip()
    except:
        return None


sum = 0
while (l := ll()) is not None:
    if not l:
        continue

    seqs = [[int(x) for x in l.split()]]
    while True:
        for x in seqs[-1]:
            if x != 0:
                break
        else:
            break

        seqs.append([])
        for i in range(len(seqs[-2]) - 1):
            seqs[-1].append(seqs[-2][i + 1] - seqs[-2][i])
        print(seqs[-1])

    i = len(seqs)
    carry = 0
    while i > 0:
        i -= 1
        carry = seqs[i][0] - carry
    sum += carry
print(sum)
