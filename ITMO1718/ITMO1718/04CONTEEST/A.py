n = int(input())
lst = list(map(int, input().split()))
lst.sort()
ans = 1
max_ans = 1
for i in range(1, n):
    if lst[i - 1] * 2 > lst[i]:
        ans += 1
    else:
        max_ans = max(ans, max_ans)
        ans = 1
print(max(ans, max_ans))