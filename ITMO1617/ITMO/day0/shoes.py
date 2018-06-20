size = int(input())
n = int(input())
lst = list(map(int, input().split()))
lst.sort()
num = 0
prev_size = -1
for i in lst:
    if i >= size:
        if prev_size >= size:
            if i - 3 >= prev_size or (i == prev_size and num == 0):
                num += 1
        else:
            num += 1
    prev_size = i
print(num)
