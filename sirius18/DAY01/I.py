size = int(input())
n = int(input())
if n == 0:
    print(0)
else:
    lst = list(map(int, input().split()))
    lst.sort()
    if lst[-1] < size:
        print(0)
    else:
        num = 0
        prev_size = -10
        for i in lst:
            if i >= size:
                if i - 3 >= prev_size:
                    num += 1
                    prev_size = i
        print(num)
