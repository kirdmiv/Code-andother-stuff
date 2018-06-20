n, r = map(int, input().split())
lst = list(map(int, input().split()))
i = 0
j = n - 1
res = 0
while i < n and j >= 0:
    if lst[j] - lst[i] >= r:
        j -= 1
        res += 1
    if lst[j] - lst[i] < r:
        i += 1
print(res)