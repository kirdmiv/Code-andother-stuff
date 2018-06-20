n ,k = map(int, input().split())
a = [i for i in range(1, n+ 1)]
c = [0] * n
r = -1
for i in range(k):
    t = int(input())
    t -= 1
    tm = a[t]
    zxzx= a.index(a[i])
    if tm == 1 and r < tm - 1:
        r = tm
    if r == tm - 1:
        r = tm
    if c[t] < c[zxzx]:
        a[t] += 1
        a[zxzx] -= 1
    c[t] += 1

print(*a)