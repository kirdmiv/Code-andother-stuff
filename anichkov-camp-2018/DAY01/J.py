import sys

sys.setrecursionlimit(10 ** 9)


def dfs(u):
    if u == n - 1:
        return "YES"
    used[u] = True
    for k in graph[u]:
        if not used[k] and dfs(k) == "YES":
            return "YES"
    return "NO"


fin = open("path.in", 'r')
fout = open("path.out", 'w')

n, m = map(int, fin.readline().split())
weight = int(fin.readline())
graph = [[] for i in range(n)]
used = [False] * n

for i in range(m):
    u, v, w = map(int, fin.readline().split())
    u -= 1
    v -= 1
    if w >= weight:
        graph[u].append(v)
        graph[v].append(u)

#print(graph)
print(dfs(0), file=fout)

fin.close()
fout.close()
