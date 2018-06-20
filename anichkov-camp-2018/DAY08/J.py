fin = open("journey.in", 'r')
fout = open("journey.out", 'w')

n, t = map(int, fin.readline().split())
w = list(map(int, fin.readline().split()))
d = list(map(int, fin.readline().split()))
p = list(map(int, fin.readline().split()))

ar = [()] * n
for i in range(n):
    ar[i] = (p[i] - (d[i] * t), i)
for i in range(n):
    w[i] = (w[i], i)
w.sort()
ar.sort()
ans = [0] * n
for i in range(n):
    ans[ar[i][1]] = w[i][1] + 1
print(*ans, file=fout)
fin.close()
fout.close()
