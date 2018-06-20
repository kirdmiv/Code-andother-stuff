n, m = map(int, input().split())
a = list(map(int, input().split()))

ans = [0] * n
if a[0] == -1:
    ans[0] = m
    a[0] = m
else:
    ans[0] = a[0]
for i in range(1, n):
    if a[i] != -1:
        if a[i] - a[i-1] < m:
            print(-1)
            exit()
        else:
            ans[i] = a[i] - a[i-1]
    else:
        a[i] = a[i-1] + m
        ans[i] = m

print(*ans)