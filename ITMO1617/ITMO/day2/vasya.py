num = int(input())
lst = []
for i in range(num):
    a, n = map(int, input().split())
    for j in range(n):
        lst.append(a)
i = 0
j = len(lst) - 1
while i + 1 < j:
    if lst[i] < lst[j]:
        lst[i + 1] += lst[i]
        lst[j - 1] += lst[i]
        lst[j] -= lst[i]
        lst[i] = 0
        i += 1
        if lst[j] == 0:
            j -= 1
    else:
        lst[i + 1] += lst[j]
        lst[j - 1] += lst[j]
        lst[i] -= lst[j]
        lst[j] = 0
        j -= 1
        if lst[i] == 0:
            i += 1
res = j - i + 1
print(res)
if res == 2:
    print(lst[i], lst[j])
else:
    print(lst[i])
