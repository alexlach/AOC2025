lines = open("01/input.txt").read().splitlines()

position, land, cross = 50, 0, 0

for line in lines:
    amt = int(line[1:])
    if line[0] == "R":
        cross += (position + amt) // 100
        position = (position + amt) % 100
    else:
        cross += (-position % 100 + amt) // 100
        position = (position - amt) % 100
    if position == 0:
        land += 1

print(land)
print(cross)
