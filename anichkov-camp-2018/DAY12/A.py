n, k = map(int, input().split())
a = list(input().split())

res = []

for i in range(n):
    tmp = a[i]
    for j in range(len(tmp)):
        res.append((10 ** (len(tmp) -1 - j)) * (9- int(tmp[j])))

res.sort(reverse=True)
ans = 0
for i in range(min(k, len(res))):
    ans += res[i]
print(ans)
