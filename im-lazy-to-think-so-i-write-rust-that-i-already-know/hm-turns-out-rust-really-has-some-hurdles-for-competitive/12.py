def ll():
    try:
        return input().strip()
    except:
        return None


cache = {}


def f(text, first_available, nums, prefix):
    seg_len = nums[len(prefix)]
    do_break = False
    rv = 0
    k = (len(prefix), first_available)
    if k in cache:
        # print("cache hit", k, cache[k])
        return rv + cache[k]
    for start_i in range(first_available, len(text) - seg_len + 1):
        if do_break:
            break

        if text[start_i] == ".":
            continue

        if text[start_i] == "#":
            do_break = True

        fits = True
        for k in range(start_i, start_i + seg_len):
            if text[k] == ".":
                fits = False
        if not fits:
            continue

        if len(prefix) + 1 == len(nums):
            for h in range(start_i + seg_len, len(text)):
                if text[h] == "#":
                    break
            else:
                rv += 1
            continue

        if start_i + seg_len < len(text) and text[start_i + seg_len] != "#":
            rv += f(text, start_i + seg_len + 1, nums, prefix + (start_i,))

    cache[(len(prefix), first_available)] = rv
    return rv


s = 0
while (l := ll()) is not None:
    if not l:
        continue
    a, b = l.split()
    nums = [int(x) for x in b.split(",")]
    cache = {}
    s += f("?".join(a for _ in range(5)), 0, nums * 5, ())
print(s)
