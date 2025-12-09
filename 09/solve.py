from itertools import combinations, pairwise

lines = open("09/input.txt").read().splitlines()
coords = [tuple(map(int, line.split(","))) for line in lines]
pairs = list(combinations(coords, 2))
calc_area = lambda p1, p2: (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)
print(f"Max area is {max(calc_area(*p) for p in pairs)}")  # part 1

closed_coords = coords + [coords[0]]
max_area = 0
for p1, p2 in pairs:
    min_x, max_x = sorted([p1[0], p2[0]])
    min_y, max_y = sorted([p1[1], p2[1]])

    # check if any line segment overlaps with our rectangle
    for (x1, y1), (x2, y2) in pairwise(closed_coords):
        if not (
            max(x1, x2) <= min_x
            or max_x <= min(x1, x2)
            or max(y1, y2) <= min_y
            or max_y <= min(y1, y2)
        ):
            break  # no intersection found, so this is a valid rectangle
    else:
        max_area = max(max_area, calc_area(p1, p2))

print(f"Max area is {max_area}")  # part 2
