INF = 10 ** 9 + 7

fin = open("gas.in", 'r')
fout = open("gas.out", 'w')

n, b = map(int, fin.readline().split())
z = [[]] * n
dp = [-1] * n
dp[0] = 0
for i in range(n):
    x, c = map(int, fin.readline().split())
    z[i] = [x, c]

for i in range(n):
    if dp[i] != -1:
        for j in range(i + 1, n):
            r = z[j][0] - z[i][0]
            if r <= b:
                if dp[j] == -1:
                    dp[j] = dp[i] + (r * z[i][1])
                else:
                    dp[j] = min(dp[j], dp[i] + (r * z[i][1]))
            else:
                break

print(dp[-1], file=fout)
fin.close()
fout.close()