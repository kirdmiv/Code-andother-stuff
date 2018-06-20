n = int(input())
lst1 = list(map(int, input().split()))
m = int(input())
lst2 = list(map(int, input().split()))
i = 0
j = 0
res = (lst1[i], lst2[j])
while i < n and j < m:
    if lst1[i] < lst2[j]:
        if abs(lst1[i] - lst2[j]) < abs(res[0] - res[1]):
            res = (lst1[i], lst2[j])
        i += 1
    elif lst1[i] > lst2[j]:
        if abs(lst1[i] - lst2[j]) < abs(res[0] - res[1]):
            res = (lst1[i], lst2[j])
        j += 1
    elif lst1[i] == lst2[j]:
        res = (lst1[i], lst2[j])
        break
print(*res)
