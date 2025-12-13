data = open("12/input.txt").read().split("\n\n")[-1]
data = data.replace(":", "").replace("x", " ")

total = 0
for line in data.splitlines():
    width, height, *counts = map(int, line.split())
    total += sum(counts) <= (width // 3) * (height // 3)
print(total)
