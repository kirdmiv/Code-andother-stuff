n = int(input())
a = [0] * n
for i in range(n):
    a[i] = int(input())

a.reverse()

for i in range(1, n):
    if a[i] < a[i-1]:
        continue
    tmp1 = str(a[i])
    tmp2 = str(a[i-1])
    ind = 0
    for j in range(len(tmp2)):
        if tmp1[j] != tmp2[j]:
            ind = j
    for k in range(ind, len())
        mx = 0