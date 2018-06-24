INF = 1e9

n, m = map(int, input().split())
g = [[0] * (m) for i in range(n)]
for i in range(n):
    g[i] = list(map(int, input().split()))


for i in range(n):
    for j in range(m):
        if i != 0 and j != 0:
            g[i][j] += min(g[i-1][j], g[i][j-1])
        elif i == 0 and j != 0:
            g[i][j] += g[i][j-1]
        elif i != 0 and j == 0:
            g[i][j] += g[i-1][j]


print(g[-1][-1])