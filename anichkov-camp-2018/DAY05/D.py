def stupid(i, j):
    if dp[i][j] >= 0:
        return dp[i][j]
    dp[i][j] = 0
    if i > 1 and j > 0:
        dp[i][j] += stupid(i - 2, j - 1)
    if i > 1 and j < m - 1:
        dp[i][j] += stupid(i - 2,j + 1)
    if i > 0 and j > 1:
        dp[i][j] += stupid(i - 1, j - 2)
    if i < n - 1 and j > 1:
        dp[i][j] += stupid(i + 1, j - 2)
    return dp[i][j]

INF = 10 ** 9 + 7

fin = open("knight2.in", 'r')
fout = open("knight2.out", 'w')

n, m = map(int, fin.readline().split())

dp = [[-1] * m for i in range(n)]
dp[0][0] = 1
print(stupid(n-1, m-1), file=fout)

fin.close()
fout.close()
