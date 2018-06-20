import sys

sys.setrecursionlimit(10 ** 6)


def dfs(graph, vertex, used, prev):
    used[vertex] = True
    for i in range(len(graph[vertex])):
        if graph[vertex][i] and not used[i]:
            t = dfs(graph, i, used, vertex)
            if t == 1:
                return 1
        elif graph[vertex][i] and used[i] and i != prev:
            return 1
    return 0


dfs_in = open('input.txt', 'r')
dfs_out = open('output.txt', 'w')

n = int(dfs_in.readline())
graph = []
for i in range(n):
    graph.append(list(map(int, dfs_in.readline().split())))
dfs_in.close()

tmp = 0
for i in range(n):
    used = [False] * n
    t = dfs(graph, i, used, i)
    if t > tmp:
        tmp = t
print(tmp, file=dfs_out)
dfs_out.close()
