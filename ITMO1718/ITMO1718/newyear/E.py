n, t = map(int, input().split())
a = list(map(int, input().split()))

ans = [i for i in range(n)] + ([-1] * (t + 1))

print(ans)


for i in range(1, t + 1):

    print(ans, a[-i] - 1, ans[-i], i)
    if ans[a[-i] - 1] >= 0:
        ans[-i] = a[-i] - 1
        ans[a[-i] - 1] = -1

print(ans)
for i in ans:
    if i >= 0:
        print(i + 1, end=" ")