n = int(input())
k = int(input())
lstk = list(map(int, input().split()))
lst = [0] * n
if 1 not in lstk:
    lst[0] = 1
if 2 not in lstk:
    lst[1] = 2
for i in range(2, n):
    if i + 1 not in lstk:
        lst[i] = lst[i - 2] + lst[i - 1]
print(lst[n - 1])
