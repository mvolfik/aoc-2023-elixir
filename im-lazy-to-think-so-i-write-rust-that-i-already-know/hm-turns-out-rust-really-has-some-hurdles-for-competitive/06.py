l1 = [int(x) for x in input().split()[1:]]
l2 = [int(x) for x in input().split()[1:]]

x = 1
for i in range(len(l1)):
    a = l1[i]
    b = l2[i]
    n = 0
    for j in range(1, a):
        d = j*(a-j)
        if d > b:
            n += 1
    x *= n
print(x)