fin = open("ones.in", 'r')
fout = open("ones.out", 'w')

n = int(fin.readline().rstrip())

if n == 1:
    print(2, file=fout)
    exit()
if n == 2:
    print(4, file=fout)
    exit()
if n == 3:
    print(7, file=fout)
    exit()

dp = [0] * n
dp[0] = 2
dp[1] = 4
dp[2] = 7
for i in range(3, n):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
print(dp[-1], file=fout)
fin.close()
fout.close()
