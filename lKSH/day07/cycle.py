import sys

sys.setrecursionlimit(10 ** 6)


def dfs(graph, vertex, prev, color):
    color[vertex] = 1
    for i in range(len(graph[vertex])):
        if color[i] == 1 and i != vertex:
            return 1
        elif color[i] == 0:
            return dfs(graph, i, vertex, color)
    color[vertex] = 2
    return 0


cycle_in = open('cycle.in', 'r')
cycle_out = open('cycle.out', 'w')

n = int(cycle_in.readline())
graph = []
for i in range(n):
    graph.append(list(map(int, cycle_in.readline().split())))
cycle_in.close()

color = [0] * n
t = dfs(graph, 0, 0, color)
print(t, file=cycle_out)
cycle_out.close()
