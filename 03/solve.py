banks = open("03/input.txt").read().splitlines()


def max_number(line, max_digits):
    result = ""
    start = 0
    for remaining in range(max_digits, 0, -1):
        end = len(line) - remaining
        best = line.index(max(line[start : end + 1]), start)
        result += line[best]
        start = best + 1
    return int(result)


print(sum(max_number(bank, 2) for bank in banks))  # part 1
print(sum(max_number(bank, 12) for bank in banks))  # part 2
