fin = open("che.in", 'r')
fout = open("che.out", 'w')

n, r = map(int, fin.readline().split())
a = list(map(int, fin.readline().split()))
f = 0
s = 0
ans = 0
for j in range(n):
    flag = False
    st = a[j]
    d = st + r
    for i in range(s, n):
        if a[i] > d:
            s = i
            flag = True
            break
    if not flag:
        break
    ans += n - s
print(ans, file=fout)
fin.close()
fout.close()