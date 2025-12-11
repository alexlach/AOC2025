from collections import defaultdict

lines = open("11/input.txt").read().splitlines()

graph = defaultdict(list)
for line in lines:
    key, vals = line.split(": ")
    graph[key].extend(vals.split())


def find_paths(node, path):
    if node == "out":
        return [path]
    return [p for n in graph[node] for p in find_paths(n, path + [n])]


print(len(find_paths("you", ["you"])))
