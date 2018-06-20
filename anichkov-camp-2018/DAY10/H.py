def gen(k1, last):
    if k1 == k:
        print(*a, file=fout)
        return
    for i in range(last+1, n+1):
        if not used[i]:
            a[k1] = i
            used[i] = True
            gen(k1+1, i)
            used[i] = False
            a[k1] = 0

fin = open("choose.in", 'r')
fout = open("choose.out", 'w')

n, k = map(int, fin.readline().split())
a = [0] * k
ans = []
used = [False] * (n+1)
gen(0, 0)
fin.close()
fout.close()
