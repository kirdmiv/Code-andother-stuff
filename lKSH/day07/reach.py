import sys

sys.setrecursionlimit(10 ** 6)


def dfs(graph, vertex, used):
    used[vertex] = True
    for i in range(1, len(graph[vertex])):
            if not used[graph[vertex][i] - 1]:
                dfs(graph, graph[vertex][i] - 1, used)
    return used


reach_in = open('reach.in', 'r')
reach_out = open('reach.out', 'w')

n, s = map(int, reach_in.readline().split())
graph = []
for i in range(n):
    graph.append(list(map(int, reach_in.readline().split())))
reach_in.close()

used = [False] * (n + 1)
t = dfs(graph, s - 1, used)
print(t.count(True), file=reach_out)
reach_out.close()
