import sys

sys.setrecursionlimit(10 ** 6)


def components(graph, used):
    res = 0
    for i in range(len(used)):
        if not used[i]:
            dfs(graph, i, used)
            res += 1
    return res


def dfs(graph, vertex, used):
    used[vertex] = True
    for i in range(len(graph[vertex])):
        if graph[vertex][i] and not used[i]:
            dfs(graph, i, used)


components_in = open('components.in', 'r')
components_out = open('components.out', 'w')

n = int(components_in.readline())
graph = []
for i in range(n):
    graph.append(list(map(int, components_in.readline().split())))
components_in.close()

used = [False] * n
print(components(graph, used), file=components_out)
components_out.close()
