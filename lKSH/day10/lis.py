def lis(lst, n):
    lis = [1] * n
    for i in range(1, n):
        for j in range(i):
            if lst[i] > lst[j] and lis[i] <= lis[j]:
                lis[i] = lis[j] + 1
    return max(lis)


lis_in = open('lis.in', 'r')
lis_out = open('lis.out', 'w')

n = int(lis_in.readline())
lst = list(map(int, lis_in.readline().split()))
lis_in.close()

print(lis(lst, n), file=lis_out)
lis_out.close()