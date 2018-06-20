n = int(input())
lst = [0] * n
lst[0] = 0
lst[1] = 1
lst[2] = 1
for i in range(3, n):
    lst[i] = lst[i - 3] + lst[i - 2]
print(lst[n - 1])
