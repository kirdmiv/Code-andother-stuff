n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in range(0, (n // 3) * 3, 3):
    ans += a[i] + a[i + 1] + a[i + 2] - min(a[i], a[i + 1], a[i + 2])

for i in range((n // 3) * 3, n):
    if a[i] > 0:
        ans += a[i]

print(ans)
