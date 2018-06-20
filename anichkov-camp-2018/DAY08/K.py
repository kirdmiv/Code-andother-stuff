fin = open("shop.in", 'r')
fout = open("shop.out", 'w')

n, k = map(int, fin.readline().split())
a = list(map(int, fin.readline().split()))
a.sort(reverse=True)
s = 0
ans = 0
cnt = 0
for i in range(n):
    cnt += 1
    s += a[i]
    if cnt == k:
        ans += s - a[i]
        s = 0
        cnt = 0
ans += s
print(ans, file=fout)
fin.close()
fout.close()
