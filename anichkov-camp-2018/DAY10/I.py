build_in = open('num2brackets.in', 'r')
build_out = open('num2brackets.out', 'w')

# Читаем
n, k = map(int, build_in.readline().split())
dp = [[0] * (n + 1) for i in range(n * 2 + 1)]
dp[0][0] = 1
build_in.close()

for i in range(2 * n):
    for j in range(n + 1):
        if j + 1 <= n:
            dp[i + 1][j + 1] += dp[i][j]
        if j > 0:
            dp[i + 1][j - 1] += dp[i][j]

ans = ""
depth = 0
for i in range(n * 2 - 1, -1, -1):
    if depth + 1 <= n and dp[i][depth + 1] >= k:
        ans += '('
        depth += 1
    else:
        ans += ')'
        if depth + 1 <= n:
            k -= dp[i][depth + 1]
        depth -= 1
print(ans, file=build_out)
build_out.close()