fin = open("cobbler.in", 'r')
fout = open("cobbler.out", 'w')

k, n = map(int, fin.readline().split())
a = list(map(int, fin.readline().split()))
a.sort()
s = 0
cnt = 0
for i in range(n):
    if s + a[i] <= k:
        s += a[i]
        cnt += 1
print(cnt, file=fout)
fin.close()
fout.close()
