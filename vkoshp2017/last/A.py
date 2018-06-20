a = list(map(int, input().split()))
n = a[0]
a = a[1:]
a *= 3
k = n
dp = [[0] * n for l in range(n)]
for h in range(n):
    dp[1][h] = abs(a[k + h - 1] -a[k + h])
for i in range(2, n):
    for j in range(n):
        tmp1 = abs(a[k + j - i] - a[k + j - i + 1])
        tmp2 = abs(a[k + j - i] - a[k + j])
        dp[i][j] = max(dp[i-1][j] + tmp1, dp[i-1][j-1] + tmp2)
        print(i, j, tmp1, tmp2, dp[i-1][j] + tmp1, dp[i-1][j-1] + tmp2)

print(max(dp[-1]))
print(dp, a, k)