from itertools import combinations

lines = open("08/input.txt").read().splitlines()
points = [tuple(map(int, line.split(","))) for line in lines]

# ordered_distances = [(distance, i, j), ...]; i and j are the indices of the points
get_distance = lambda p1, p2: sum((a - b) ** 2 for a, b in zip(p1, p2))
ordered_distances = sorted(
    (get_distance(points[i], points[j]), i, j)
    for i, j in combinations(range(len(points)), 2)
)

circuits = [{i} for i in range(len(points))]  # each box starts on its own circuit
find = lambda p: next(c for c in circuits if p in c)  # find circuit containing point p

for n, (_, i, j) in enumerate(ordered_distances, 1):
    circuit_i, circuit_j = find(i), find(j)

    if circuit_i is not circuit_j:  # merge the two circuits
        circuit_i.update(circuit_j)
        circuits.remove(circuit_j)
        if len(circuits) == 1:  # part 2 (we found our final pair to connect)
            print(points[i][0] * points[j][0])

    if n == 1000:  # part 1 (we found our 1000th pair)
        sizes = sorted(len(circuit) for circuit in circuits)
        print(sizes[-1] * sizes[-2] * sizes[-3])
