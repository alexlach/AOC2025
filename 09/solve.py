from itertools import combinations

lines = open("09/input.txt").read().splitlines()
coords = [tuple(map(int, line.split(","))) for line in lines]
print(f"Red tiles are at {coords}")


def calc_area(coord_i, coord_j):
    return (abs(coord_i[0] - coord_j[0]) + 1) * (abs(coord_i[1] - coord_j[1]) + 1)


areas = max(calc_area(coord_i, coord_j) for coord_i, coord_j in combinations(coords, 2))
print(f"Maximum area is {areas}")
