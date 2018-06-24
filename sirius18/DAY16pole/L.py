a = list(map(int, input().split()))
a.sort()
cnt = 0
ans = 0
for i in range(4):
    if a[i] + cnt <= 4:
        cnt += a[i]
    else:
        ans += 1

if (cnt < 2):
    ans = max(1, ans)
print(ans)