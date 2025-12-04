lines = open("04/input.txt").read().splitlines()
grid = {(r, c): char for r, row in enumerate(lines) for c, char in enumerate(row)}

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def count_neighbors(row, col):
    """Count the number of @ neighbors for a given position, looking in eight directions"""
    return sum(grid.get((row + dr, col + dc)) == "@" for dr, dc in directions)


def remove_accessible_rolls():
    accessible_rolls = [
        pos for pos, char in grid.items() if char == "@" and count_neighbors(*pos) < 4
    ]
    for pos in accessible_rolls:
        grid[pos] = "."
    return len(accessible_rolls)


print(remove_accessible_rolls())  # part 1

grid = {(r, c): ch for r, line in enumerate(lines) for c, ch in enumerate(line)}
print(sum(iter(remove_accessible_rolls, 0)))  # part 2
