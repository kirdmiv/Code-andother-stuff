def number(n):
    dp = [[0] * 10 for i in range(n)]
    dp[0][0] = 0
    for i in range(1, 10):
        dp[0][i] = 1
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + dp[i - 1][1]
        for j in range(1, 9):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] + dp[i - 1][j + 1]
        dp[i][9] = dp[i - 1][8] + dp[i - 1][9]
    return sum(dp[n - 1])


numbers_in = open('numbers.in', 'r')
numbers_out = open('numbers.out', 'w')

n = int(numbers_in.readline())
numbers_in.close()

print(number(n), file=numbers_out)
numbers_in.close()
