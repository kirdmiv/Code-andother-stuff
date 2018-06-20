INF = 10 ** 9 + 7
fin = open("bwhite.in", 'r')
fout = open("bwhite.out", 'w')

n, k = map(int, fin.readline().split())
g = [[]] * n
for i in range(n):
    g[i] = list(map(int, fin.readline().split()))
dp = [[0] * k for i in range(n)]
d = [[0] * k for i in range(n)]
for i in range(0, n):
    for j in range(0, k):
        if g[i][j] == 1:
            dp[i][j] = 0
        else:
            if i > 0:
                dp[i][j] = dp[i - 1][j] + 1
            else:
                dp[i][j] = 1
for i in range(0, n):
    for z in range(0, k):
        mn = INF
        for j in range(z, k):
            mn = min(mn, dp[i][j])
            d[i][z] = max(d[i][z], mn * (j-z+1))

mx = 0
for i in d:
    mx = max(mx, max(i))

print(mx, file=fout)
fin.close()
fout.close()
