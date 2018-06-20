fin = open("lcs.in", 'r')
fout = open("lcs.out", 'w')

n = int(fin.readline().rstrip())
a1 = list(map(int, fin.readline().split()))
m = int(fin.readline().rstrip())
a2 = list(map(int, fin.readline().split()))

dp = [[0] * (m + 1) for i in range(n + 1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        if a1[i-1] == a2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[n][m], file=fout)
fin.close()
fout.close()
