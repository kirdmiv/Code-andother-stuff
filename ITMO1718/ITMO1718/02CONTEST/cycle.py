def dfs(u, vert):
    visited[u] = True
    path[u] = path[vert].append(u + 1)
    for i in lst[u]:
        if not visited[i]:
            b, ppaatthh = dfs(i, u)
            if b:
                return b, ppaatthh
        else:
            return True, path[u]
    return False, []


fin = open("cycle.in", 'r')
fout = open("cycle.out", 'w')

n, m = map(int, fin.readline().split())
lst = [[] for i in range(n)]
visited = [False for i in range(n)]
path = [[] for i in range(n)]
for i in range(m):
    k, j = map(int, fin.readline().split())
    if not (j - 1 in lst[k - 1]):
        lst[k - 1].append(j - 1)

print(lst)
print(dfs(0, 0), file=fout)
fout.close()
fin.close()
