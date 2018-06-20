import sys
sys.setrecursionlimit(10**9)

def dfs(u, ti, to):
    tin[u] = ti + 1
    l = to
    for v in graph[u]:
        to, ti = dfs(v, ti+1, to)
    tout[u] = to + 1
    return to + 1, ti + 1


fin = open("ancestor.in", 'r')
fout = open("ancestor.out", 'w')

n = int(fin.readline())
lst = list(map(int, fin.readline().split()))
graph = [[] for k in range(n)]
tin = [0] * n
tout = [0] * n
for j in range(n):
    if lst[j] == 0:
        start = j
    else:
        graph[lst[j] - 1].append(j)

print(graph)
dfs(start, 0, 0)

print(tin, tout)
m = int(fin.readline())
for i in range(m):
    a, b = map(int, fin.readline().split())
    if (tin[a - 1] < tin[b - 1]) and (tout[a - 1] > tout[b - 1]):
        print(1, file=fout)
    else:
        print(0, file=fout)
fin.close()
fout.close()
