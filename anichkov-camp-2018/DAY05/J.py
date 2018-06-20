fin = open("knapsack.in", 'r')
fout = open("knapsack.out", 'w')

s, n = map(int, fin.readline().split())
a = list(map(int, fin.readline().split()))

dp = [[-1] * (s+1) for i in range(n+1)]

for i in range(n+1):
    dp[i][0] = 0
for i in range(s+1):
    dp[0][i] = 0

for i in range(1, n+1):
    for j in range(1, s+1):
        if j >= a[i-1]:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - a[i-1]] + a[i-1])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[-1][-1], file=fout)
fin.close()
fout.close()
