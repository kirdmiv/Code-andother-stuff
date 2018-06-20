def bisel(x):
    isHere = False
    l = -1
    r = n
    while r - l > 1:
        m = (l + r) // 2
        if a[m] < x:
            l = m
        else:
            r = m
            if a[m] == x:
                isHere = True
    if isHere:
        return r
    return -2

def biser(x):
    isHere = False
    l = -1
    r = n
    while r - l > 1:
        m = (l + r) // 2
        if a[m] <= x:
            l = m
            if a[m] == x:
                isHere = True
        else:
            r = m
    if isHere:
        return l
    return -2



fin = open("binsearch.in", 'r')
fout = open("binsearch.out", 'w')

n = int(fin.readline().rstrip())
a = list(map(int, fin.readline().split()))
m = int(fin.readline().rstrip())
lst = list(map(int, fin.readline().split()))
for x in lst:
    print(bisel(x) + 1, biser(x) + 1, file=fout)

fin.close()
fout.close()