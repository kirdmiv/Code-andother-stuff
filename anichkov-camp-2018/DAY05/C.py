INF = 10 ** 9 + 7

fin = open("knight.in", 'r')
fout = open("knight.out", 'w')

n, m = map(int, fin.readline().split())

dp = [[0] * m for i in range(n)]
dp[0][0] = 1
for i in range(1, n):
    for j in range(1, m):
        if i > 1:
            dp[i][j] += dp[i-2][j-1]
        if j > 1:
            dp[i][j] += dp[i-1][j-2]

#print(dp)
print(dp[-1][-1], file=fout)

fin.close()
fout.close()
