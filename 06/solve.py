from math import prod

lines = open("06/input.txt").read().splitlines()

# part 1
operator_line = lines[-1].split()
rows = [[int(n) for n in line.split()] for line in lines[:-1]]
columns = list(zip(*rows))

total = 0
for op, col in zip(operator_line, columns):
    total += sum(col) if op == "+" else prod(col)
print(total)

# part 2
max_len = max(len(line) for line in lines)
total = 0
nums = []
for col in range(max_len - 1, -1, -1):
    digit = "".join(row[col] for row in lines[:-1] if row[col].isdigit())
    if digit:
        nums.append(int(digit))

    op = lines[-1][col]
    if op in "+*":
        total += sum(nums) if op == "+" else prod(nums)
        nums = []

print(total)
