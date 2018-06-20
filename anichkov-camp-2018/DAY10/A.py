def gen(k,one):
    if k == n:
        ans.append(a[:])
        return
    a[k] = 0
    gen(k+1, False)
    a[k] = 1
    gen(k + 1, True)


fin = open("vectors.in", 'r')
fout = open("vectors.out", 'w')

n = int(fin.readline())
a = [0] * n
ans = []
gen(0, False)
print(len(ans), file=fout)
for i in ans:
    print(*i, sep="", file=fout)
fin.close()
fout.close()
