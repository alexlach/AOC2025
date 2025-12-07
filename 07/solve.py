from collections import Counter

lines = open("07/input.txt").read().splitlines()
tachyons = Counter([lines.pop(0).index("S")])

split_count = 0
tachyon_count = 1
for line in lines:
    new_tachyons = Counter()
    for pos, count in tachyons.items():
        if line[pos] == "^":
            new_tachyons[pos - 1] += count
            new_tachyons[pos + 1] += count
            split_count += 1
            tachyon_count += count
        else:
            new_tachyons[pos] += count
    tachyons = new_tachyons

print(split_count)  # part 1
print(tachyon_count)  # part 2
