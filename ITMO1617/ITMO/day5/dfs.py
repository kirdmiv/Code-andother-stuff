import sys

sys.setrecursionlimit(10 ** 6)


def dfs(graph, vertex, used):
    used[vertex] = True
    for i in range(len(graph[vertex])):
        if graph[vertex][i] and not used[i]:
            dfs(graph, i, used)
    return used


dfs_in = open('input.txt', 'r')
dfs_out = open('output.txt', 'w')

n, s = map(int, dfs_in.readline().split())
graph = []
for i in range(n):
    graph.append(list(map(int, dfs_in.readline().split())))
dfs_in.close()

used = [False] * n
t = dfs(graph, s - 1, used)
print(t.count(True), file=dfs_out)
dfs_out.close()
