n, k = map(int, input().split())
a = list(map(int, input().split()))

res = 0
ans = (0, 0)
suffmax = [(a[n-1], n-1)] * n
for i in range(n-2, -1, -1):
    if suffmax[i+1][0] > a[i]:
        suffmax[i] = suffmax[i+1]
    else:
        suffmax[i] = (a[i], i)

for i in range(0, n-k):
    if res < a[i] + suffmax[i+k][0]:
        res = a[i] + suffmax[i+k][0]
        ans = (i+1, suffmax[i+k][1]+1)
print(*ans)