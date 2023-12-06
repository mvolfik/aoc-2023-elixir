a = int("".join(input().split()[1:]))
b = int("".join(input().split()[1:]))

n = 0
for j in range(1, a):
    d = j*(a-j)
    if d > b:
        n += 1
print(n)
