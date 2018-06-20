INF = 10 ** 9 + 7
fin = open("mutants2.in", 'r')
fout = open("mutants2.out", 'w')

n, m = map(int, fin.readline().split())
g = [[]] * n
for i in range(n):
    g[i] = list(map(int, fin.readline().split()))
prev = [[[0, 0]] * m for i in range(n)]
dp = [[-1] * m for i in range(n)]

#print(g, prev, dp, n, m)
s = 0
for i in range(n):
    s += g[i][0]
    dp[i][0] = s
    prev[i][0] = (i-1, 0)
s = 0
for i in range(m):
    s += g[0][i]
    dp[0][i] = s
    prev[0][i] = (0, i-1)

for i in range(1, n):
    for j in range(1, m):
        if dp[i-1][j] < dp[i][j-1]:
            dp[i][j] = dp[i-1][j] + g[i][j]
            prev[i][j] = (i-1, j)
        else:
            dp[i][j] = dp[i][j - 1] + g[i][j]
            prev[i][j] = (i, j - 1)

print(dp[-1][-1], file=fout)
path = [(n, m)]
i = n-1
j = m-1
while i > 0 or j > 0:
    i, j = prev[i][j][0], prev[i][j][1]
    path.append((i+1, j+1))
path.reverse()
print(len(path), file=fout)
for i in path:
    print(*i, file=fout)

fin.close()
fout.close()
