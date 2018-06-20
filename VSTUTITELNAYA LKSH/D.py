n, ks = map(int, input().split())
a = list(map(int, input().split()))

if n <= ks <= 2 * n:
    dp = [[0] * (n+1) for i in range(n+1)]
    for i in range(1, n+1):
        dp[i][0] = a[i-1]
    for i in range(1, n+1):
        for j in range(1, i):
            for k in range(1, i+1):
                if dp[j][k-1] != 0 and  dp[i-j][0] != 0:
                    dp[i][k] = max(dp[i][k], dp[j][k-1] + dp[i-j][0])
    mx = dp[-1][ks-n-1]
    for i in range(ks-n, n+1):
        mx = max(mx, dp[-1][i])
    print(mx)
else:
    print("Impossible")
