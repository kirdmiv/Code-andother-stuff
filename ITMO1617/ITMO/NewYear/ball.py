n = int(input())
lst = [0] * (n + 4)
lst[0] = 1
for i in range(0, n + 1):
    lst[i + 1] += lst[i]
    lst[i + 2] += lst[i]
    lst[i + 3] += lst[i]
print(lst[n])
