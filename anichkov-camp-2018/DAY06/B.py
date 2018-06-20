def dfs(u):
    used[u] = True
    for i in range(n):
        if graph[u][i] == 1 and not used[i]:
            dfs(i)
    return

fin = open("matrix.in", 'r')
fout = open("matrix.out", 'w')

n = int(fin.readline().rstrip())
used = [False] * n
graph = [[]] * n
for i in range(n):
    graph[i] = list(map(int, fin.readline().split()))

cnt = 0
for i in range(n):
    if not used[i]:
        cnt += 1
        dfs(i)
print(cnt, file=fout)
fin.close()
fout.close()
