def dfs(v):
    for i in graph[v]:
        dfs(i)
    for i in graph[v]:
        d[v][0] += max(d[i][0], d[i][1])
        dnew = d[i][0]
        for j in graph[i]:
            


n = int(input())
graph = [[] for i in range(n)]
d = [[0, 0]for i in range(n)]
for i in range(n):
    t = int(input())
    if t == 0:
        start = t
    else:
        graph[t-1] = i

