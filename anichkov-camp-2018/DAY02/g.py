EPS = 10 ** -9


def funkcia(x):
    hi1 = a
    hi = x
    for i in range(n):
        hih = (hi + 1) * 2 - hi1
        hi1 = hi
        hi = hih
        if hih <= EPS:
            return False
    return True


def bin_search():
    l = 0
    r = a
    for i in range(1000):
        m = (l + r) / 2
        if funkcia(m):
            r = m
        else:
            l = m
    return l


fin = open("garland.in", 'r')
fout = open("garland.out", 'w')

n, a = map(int, fin.readline().split())
hi1 = a
hi = bin_search()
for i in range(n):
    hih = (hi + 1) * 2 - hi1
    hi1 = hi
    hi = hih
print(hi)
fin.close()
fout.close()
