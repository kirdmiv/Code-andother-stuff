n, m = map(int, input().split())
a = list(map(int, input().split()))

dp = [[0, 0] for i in range(m)]
dp[0] = [0, a[0]]

j = k = 1

for i in range(1, m):
    dp[i][0] = max(dp[i-1])
    if dp[i-1][0] + a[0] > dp[i-1][1] + a[k % n]:
        dp[i][1] = dp[i-1][0] + a[0]
        k = 0
    else:
        dp[i][1] = dp[i-1][1] + a[k % n]
        k += 1


print(dp)
print(max((dp[-1])))