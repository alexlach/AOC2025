lines = open("02/input.txt").read().split(",")

invalid_sum = 0
invalid_ids = []

for line in lines:
    first, last = line.split("-")
    for i in range(int(first), int(last) + 1):
        left_half, right_half = str(i)[: len(str(i)) // 2], str(i)[len(str(i)) // 2 :]
        if left_half == right_half:
            invalid_sum += i

        for ind in range(len(str(i)) - 1):
            if str(i)[: ind + 1] * (len(str(i)) // (ind + 1)) == str(i):
                invalid_ids.append(i)

print(invalid_sum)
print(sum(set(invalid_ids)))
