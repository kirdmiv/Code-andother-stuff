import math

fin = open("maxnumber.in", 'r')
fout = open("maxnumber.out", 'w')

n = int(fin.readline())
a = list(map(int, fin.readline().split()))

d = {}
i = 0
while True:
    if i >= len(a):
        break
    if a[i] % 2 == 0:
        a.append(a[i] // 2)
        a.append(a[i] // 2)
    else:
        d[a[i]] = d.get(a[i], 0) + 1
    i += 1
d = list(d.items())
ans = []
#print(d)
for i in range(len(d)):
    t = d[i]
    c = t[1]
    res = t[0]
    while c > 1:
        c //= 2
        res *= 2
    ans.append(res)
print(max(ans), file=fout)
fin.close()
fout.close()
