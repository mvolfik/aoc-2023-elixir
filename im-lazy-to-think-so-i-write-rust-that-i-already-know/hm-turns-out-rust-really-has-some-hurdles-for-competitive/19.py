from collections import defaultdict


def ll():
    try:
        return input().strip()
    except:
        return None


rules = {}
while (l := ll()) is not None:
    if not l:
        break

    a, b = l[:-1].split("{")
    rules[a] = [
        (x[0], x[1], *x[2:].split(":")) if ":" in x else x for x in b.split(",")
    ]
print(rules)

s = 0
while (l := ll()) is not None:
    if not l:
        break

    nums = dict((x[0], int(x.split("=")[1])) for x in l[1:-1].split(","))
    r = "in"
    while r not in ["R", "A"]:
        rul = rules[r]
        for x in rul:
            if isinstance(x, str):
                r = x
                break
            var, comp, val, next = x
            if comp == ">":
                if nums[var] > int(val):
                    r = next
                    break
            elif comp == "<":
                if nums[var] < int(val):
                    r = next
                    break
        else:
            print("error")
            exit(1)
    if r == "A":
        s += sum(nums.values())
print(s)