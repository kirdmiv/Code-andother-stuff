fin = open("sequence.in", 'r')
fout = open("sequence.out", 'w')

n = int(fin.readline().rstrip())
a = list(map(int, fin.readline().split()))

dp = [1] * n
dp[0] = 1
for i in range(1, n):
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp), file=fout)
fin.close()
fout.close()
