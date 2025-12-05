ranges, ingredients = open("05/input.txt").read().split("\n\n")
ranges = sorted([int(x) for x in line.split("-")] for line in ranges.splitlines())
ingredients = [int(n) for n in ingredients.splitlines()]


# part 1
def in_range(n):
    return any(lo <= n <= hi for lo, hi in ranges)


print(sum(in_range(n) for n in ingredients))

# part 2
merged = [ranges[0]]  # initialize with first range
for lo, hi in ranges[1:]:
    prev_lo, prev_hi = merged[-1]
    if lo <= prev_hi + 1:
        merged[-1] = [prev_lo, max(prev_hi, hi)]
    else:
        merged.append([lo, hi])
print(sum(hi - lo + 1 for lo, hi in merged))
