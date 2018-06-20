n = int(input())
w = list(map(int, input().split()))
s = sum(w)
dp = [[False] * (s + 1) for i in range(n + 1)]
dp[0][0] = True
for i in range(1, n + 1):
    for j in range(s + 1):
        if w[i - 1] > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = dp[i - 1][j] or dp[i - 1][j - w[i - 1]]
ans = 0
for p in range(s + 1):
    if dp[n][p] and p * (s - p) > ans:
        ans = p * (s - p)
print(ans)
