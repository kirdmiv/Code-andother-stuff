import math

def f(x):
    res = x
    for i in range(2, m + 1):
        k = x // i
        if k == 0:
            break
        res += k
    #print(x, res)
    return res

def bsearch():
    l = 0
    r = n
    while r - l > 1:
        mid = (r + l) // 2
        if f(mid) < n:
            l = mid
        else:
            r = mid
    return r


fin = open("bigset.in", 'r')
fout = open("bigset.out", 'w')

n, m = map(int, fin.readline().split())

print(bsearch(), file=fout)

fin.close()
fout.close()