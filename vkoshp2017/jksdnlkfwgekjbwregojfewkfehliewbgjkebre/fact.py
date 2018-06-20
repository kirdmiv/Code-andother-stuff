a = [0] * 27
i = 1
a[0] = 1
for i in range(1, 27):
    a[i] = a[i - 1] * i
print(a)
print(a[26] / a[20])