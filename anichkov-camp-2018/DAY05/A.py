fin = open("grig.in", 'r')
fout = open("grig.out", 'w')

n, k = map(int, fin.readline().split())
dp = [0] * n
dp[0] = 1
for i in range(1, n):
    for j in range(1, min(k, i) + 1):
        dp[i] += dp[i - j]
print(dp[-1], file=fout)
fin.close()
fout.close()
