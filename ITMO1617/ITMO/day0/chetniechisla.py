n = int(input())
lst = list(map(int, input().split()))
ans = []
for i in lst:
    if i % 2 == 0:
        ans.append(i)
print(*ans)
