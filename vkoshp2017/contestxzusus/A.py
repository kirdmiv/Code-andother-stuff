def basus(x, k):
    ans = 0
    while x > 0:
        ans += x % k
        x //= k

    return ans



fin = open("groups.in", "r")
fout = open("groups.out", "w")
k, n = map(int, fin.readline().split())
a = list(map(int, fin.readline().split()))

for i in range(n):
    a[i] = basus(a[i], k)

a.sort()
res = 1
for i in range(n - 1):
    if a[i] != a[i + 1]:
        res += 1
print(res, file=fout)
fin.close()
fout.close()