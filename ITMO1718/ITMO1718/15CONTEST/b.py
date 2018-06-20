INF = 10 ** 9

n = int(input())
a = list(input())

dp = [[INF, 0, -1] for i in range(n)]
dp[0] = [0, 0, -1]

print(a, a[19])

for i in range(n):
    if a[i] == '"':
        dp[i][1] += 1
    if a[i] == 'w':
        pass
    else:
        if i < n - 2:
            if dp[i + 2][0] > dp[i][0] + 1:
                dp[i + 2][0] = dp[i][0] + 1
                dp[i + 2][1] = dp[i][1]
                dp[i+2][2] = i
            if dp[i + 2][0] == dp[i][0] + 1:
                dp[i + 2][1] = max(dp[i + 2][1], dp[i][1])
                dp[i + 2][2] = i
        if i < n - 3:
            if dp[i + 3][0] > dp[i][0] + 1:
                dp[i + 3][0] = dp[i][0] + 1
                dp[i + 3][1] = dp[i][1]
                dp[i + 3][2] = i
            if dp[i + 3][0] == dp[i][0] + 1:
                dp[i + 3][1] = max(dp[i + 3][1], dp[i][1])
                dp[i + 3][2] = i
        if i < n - 6:
            if dp[i + 6][0] > dp[i][0] + 1:
                dp[i + 6][0] = dp[i][0] + 1
                dp[i + 6][1] = dp[i][1]
                dp[i + 6][2] = i
            if dp[i + 6][0] == dp[i][0] + 1:
                dp[i + 6][1] = max(dp[i + 6][1], dp[i][1])
                dp[i + 6][2] = i


print(dp, len(dp))
l = n-1
k = dp[l][2]
path = [n]
while k != -1:
    l = k
    k = dp[l][2]
    path.append(l+1)
    print(*dp[l])
if l == 0:
    print(dp[-1][0], dp[-1][1])
    print(*path.__reversed__())
else:
    print(-1)