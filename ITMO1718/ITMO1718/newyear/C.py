x = input()
res = 0
ans = []
l = len(x)
for i in range(l-1):
    s = "9" * (l - i - 1)
    for i in range(int(x[i])):
        res += 1
        ans.append("1")
        ans.append(s)
ans.append(x[-1])
print(res)
print(*reversed(sorted(ans)))
