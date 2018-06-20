def minimum(lst):
    min = 2 * (10 ** 9)
    for i in lst:
        if min > i:
            min = i
    return min


def sub(lst, min):
    for i in range(len(lst)):
        lst[i] -= min
    return lst


def sumlst(lst, min):
    for i in range(len(lst)):
        lst[i] += min
    return lst


def cnt_sort(a):
    maxval = 100000
    cnt = [0] * maxval
    for i in a:
        cnt[i] += 1
    res = []
    for i in range(maxval):
        res += [i] * cnt[i]
    return res


marchin = open('march.in', 'r')
marchout = open('march.out', 'w')

n = marchin.readline()
lst = list(map(int, marchin.readline().split()))
marchin.close()

min = minimum(lst)
lst = sub(lst, min)
res = cnt_sort(lst)
res = sumlst(res, min)
ans = [str(i) for i in res]
ans = ' '.join(ans)
marchout.write(ans)
marchout.close()
