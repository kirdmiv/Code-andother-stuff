INF = 10 ** 9 + 7

fin = open("calcul.in", 'r')
fout = open("calcul.out", 'w')

n = int(fin.readline().rstrip())

dp = [INF] * (n + 1)
dp[1] = 0
prev = [1] * (n + 1)
for i in range(1, n + 1):
    tmp = i / 2
    if int(tmp) == tmp and dp[i] > dp[int(tmp)]:
        dp[i] = dp[int(tmp)] + 1
        prev[i] = int(tmp)
    tmp = i / 3
    if int(tmp) == tmp and dp[i] > dp[int(tmp)]:
        dp[i] = dp[int(tmp)] + 1
        prev[i] = int(tmp)
    tmp = i - 1
    if dp[i] > dp[tmp]:
        dp[i] = dp[tmp] + 1
        prev[i] = tmp
#print(prev, dp)

print(dp[-1], file=fout)

path = [n]
i = n
while i != 1:
    i = prev[i]
    path.append(i)
path.reverse()
print(*path, file=fout)
fin.close()
fout.close()
