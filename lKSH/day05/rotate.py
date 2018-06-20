def rotate(lst, high, length):
    res = [[0] * high for i in range(length)]
    for i in range(high):
        for j in range(length):
            res[j][-i - 1] = str(lst[i][j])
    return res


rotate_in = open('rotate.in', 'r')
rotate_out = open('rotate.out', 'w')

length, high = map(int, rotate_in.readline().split())
lst = [[]] * high
for i in range(high):
    lst[i] = list(map(int, rotate_in.readline().split()))
ans = rotate(lst, high, length)
for i in ans:
    print(' '.join(i), file=rotate_out)
rotate_in.close()
rotate_out.close()
