INF = int(9e9 + 7)
ans = INF
fin = open("printing.in", 'r')
fout = open("printing.out", 'w')

n = int(fin.readline().rstrip())
a1 = int(fin.readline().rstrip())
a2 = int(fin.readline().rstrip())
a3 = int(fin.readline().rstrip())
a4 = int(fin.readline().rstrip())
a5 = int(fin.readline().rstrip())
a6 = int(fin.readline().rstrip())
a7 = int(fin.readline().rstrip())

a2 = min(a2, 10 * a1)
a3 = min(a3, 10 * a2)
a4 = min(a4, 10 * a3)
a5 = min(a5, 10 * a4)
a6 = min(a6, 10 * a5)
a7 = min(a7, 10 * a6)

ans = min(ans, ((n // 1) + 1) * a1)
ans = min(ans, ((n // 10) + 1) * a2)
ans = min(ans, ((n // 100) + 1) * a3)
ans = min(ans, ((n // 1000) + 1) * a4)
ans = min(ans, ((n // 10000) + 1) * a5)
ans = min(ans, ((n // 100000) + 1) * a6)
ans = min(ans, ((n // 1000000) + 1) * a7)


cheta = n
res = 0

res += (cheta // 1000000) * a7
ans = min(ans, res + a7)
cheta %= 1000000

res += (cheta // 100000) * a6
ans = min(ans, res + a6)
cheta %= 100000

res += (cheta // 10000) * a5
ans = min(ans, res + a5)
cheta %= 10000

res += (cheta // 1000) * a4
ans = min(ans, res + a4)
cheta %= 1000

res += (cheta // 100) * a3
ans = min(ans, res + a3)
cheta %= 100

res += (cheta // 10) * a2
ans = min(ans, res + a2)
cheta %= 10

res += cheta // 1 * a1

ans = min(ans, res)

print(ans, file=fout)
fin.close()
fout.close()
