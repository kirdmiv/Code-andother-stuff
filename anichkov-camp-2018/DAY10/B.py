def gen(k):
    if k == n:
        print(*a, file=fout)
        return
    for i in range(1, n+1):
        if not used[i]:
            a[k] = i
            used[i] = True
            gen(k+1)
            used[i] = False
            a[k] = 0

fin = open("permutations.in", 'r')
fout = open("permutations.out", 'w')

n = int(fin.readline())
a = [0] * n
ans = []
used = [False] * (n+1)
gen(0)
fin.close()
fout.close()
