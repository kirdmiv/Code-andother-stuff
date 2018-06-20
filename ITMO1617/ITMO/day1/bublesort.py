len_lst = int(input())
lst = list(map(int, input().split()))
ans = 0
for i in range(0, len_lst - 1):
    for j in range(0, len_lst - i - 1):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
            ans += 1
print(ans)
