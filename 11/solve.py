from functools import cache

lines = open("11/input.txt").read().splitlines()
graph = {k: v.split() for line in lines for k, v in [line.split(": ")]}


# recursively count paths from a given node to the "out" node
def count_paths_p1(node):
    if node == "out":
        return 1
    return sum(count_paths_p1(n) for n in graph[node])


print(count_paths_p1("you"))  # part 1


# only count paths if we visit "dac" and "ftt"; memoize the results to avoid recomputing
@cache
def count_paths_p2(node, visited_dac=False, visited_fft=False):
    if node == "out":
        return visited_dac and visited_fft  # 1 if we visited both; 0 otherwise
    return sum(
        count_paths_p2(n, visited_dac or n == "dac", visited_fft or n == "fft")
        for n in graph[node]
    )


print(count_paths_p2("svr"))  # part 2
