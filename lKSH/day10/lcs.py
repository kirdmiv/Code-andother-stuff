def lcs(first_lst, second_lst, n, m):
    dp = [[0] * (m + 1) for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if first_lst[i - 1] == second_lst[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[n][m]


lcs_in = open('lcs.in', 'r')
lcs_out = open('lcs.out', 'w')

n = int(lcs_in.readline())
first_lst = list(map(int, lcs_in.readline().split()))
m = int(lcs_in.readline())
second_lst = list(map(int, lcs_in.readline().split()))
lcs_in.close()

print(lcs(first_lst, second_lst, n, m), file=lcs_out)
lcs_out.close()