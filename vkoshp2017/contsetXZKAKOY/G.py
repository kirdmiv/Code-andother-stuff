
a, b, c = map(int, input().split())
ans = 0
for i in range(1, c + 1):
    tmp1 = c // i
    tmp2 = c - (tmp1 * i)
    s = (i + 1) * tmp1
    s2 = (i + 2) * tmp1
    p1 = (i + 1) * tmp2
    p2 = (i + 2) * tmp2
    if b >= (s + p1) and a >= (s2 + p2):
        ans = max(ans, tmp1 + tmp2)
print(ans)