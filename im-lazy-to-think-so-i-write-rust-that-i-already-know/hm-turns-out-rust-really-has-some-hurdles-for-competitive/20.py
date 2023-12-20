def ll():
    try:
        return input().strip()
    except:
        return None


rules = {}
while (l := ll()) is not None:
    if not l:
        break

    name, outs = l.split(" -> ")
    outs = outs.split(", ")
    typ = "br"
    if name != "broadcaster":
        typ = name[0]
        name = name[1:]

    rules[name] = (typ, outs)

print("digraph sus {")
pm = {"br": "", "&": "A_", "%": "X_"}
for name, (typ, outs) in rules.items():
    for o in outs:
        if o in rules:
            o = pm[rules[o][0]] + o

        print(f"  {pm[typ]}{name} -> {o};")
print("}")


def init_for(t):
    if t == "%":
        return False
    if t == "&":
        return {}

    raise Exception("unknown type " + t)


state = {k: init_for(t) for k, (t, _) in rules.items() if t != "br"}

for k, (t, outs) in rules.items():
    for o in outs:
        if o not in rules:
            print("missing", o)
        if o in rules and rules[o][0] == "&":
            state[o][k] = False

outT = 0
outF = 0


def pulse(from_, name, val):
    # print(f"{from_} -{val}-> {name}")
    global outT, outF

    if val:
        outT += 1
    else:
        outF += 1

    if name not in rules:
        return

    (t, outs) = rules[name]
    if t == "br":
        for o in outs:
            yield name, o, val
    elif t == "%":
        if not val:
            s = state[name]
            for o in outs:
                yield name, o, not s
            state[name] = not s
    elif t == "&":
        s = state[name]
        assert from_ in s
        s[from_] = val

        outval = all(s.values())

        for o in outs:
            yield name, o, not outval


periods = []

for i in range(1, 5000):
    next = [("button", "broadcaster", False)]
    while len(next) > 0:
        this = next
        next = []

        for e in this:
            if e[1] in ["dh", "dp", "qd", "bb"] and not e[2]:
                periods.append(i)
            for x in pulse(*e):
                next.append(x)

import math

print(math.lcm(*periods))
