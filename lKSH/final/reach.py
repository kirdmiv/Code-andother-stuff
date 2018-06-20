import sys

sys.setrecursionlimit(10 ** 6)


def dfs(graph, vertex, used, s):
    used[vertex] = True
    if vertex == s:
        return True
    for i in range(1, len(graph[vertex])):
        if not used[graph[vertex][i] - 1]:
            if dfs(graph, graph[vertex][i] - 1, used, s):
                return True
    return False


def reach(graph, n, s):
    res = 0
    for i in range(n):
        used = [False] * (n + 1)
        if dfs(graph, i, used, s):
            res += 1
    return res


reach_in = open('reach.in', 'r')
reach_out = open('reach.out', 'w')

n, s = map(int, reach_in.readline().split())
graph = []
for i in range(n):
    graph.append(list(map(int, reach_in.readline().split())))
reach_in.close()

ans = reach(graph, n, s - 1)
print(ans, file=reach_out)
reach_out.close()
