import math

fin = open("arsenal.in", 'r')
fout = open("arsenal.out", 'w')

n = int(fin.readline().rstrip())
a = list(map(int, fin.readline().split()))
ans = []
res = 0
subres = 1
for i in range(n-1):
    if a[i] == a[i + 1]:
        subres += 1
    else:
        res += subres // 2
        subres = 1
res += math.ceil(subres / 2)
for i in range(len(a)):
    a[i] = (a[i], i)
a.sort(reverse=True)
print(res, file=fout)
i = 0
while i < n:
    el = a[i]
    z1 = z2 = i
    for j in range(i+1, n, 2):
        if el[0] != a[j][0] and el[0] != a[j-1][0]:
            z2 = j
            break
        print(a[j][1] + 1, end=" ", file=fout)
    for j in range(i, n, 2):
        if el[0] != a[j][0] and el[0] != a[j-1][0]:
            z1 = j
            break
        print(a[j][1] + 1, end=" ", file=fout)
    i += 1
    i = max(i, min(z1+1, z2+1))

fin.close()
fout.close()