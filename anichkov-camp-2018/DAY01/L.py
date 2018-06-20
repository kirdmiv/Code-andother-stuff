fin = open("tower.in", 'r')
fout = open("tower.out", 'w')

n = int(fin.readline().rstrip())
c = [()] * n

for i in range(n):
    x, l = fin.readline().split()
    x = int(x)
    if l == 'R':
        l = 0
    if l == 'G':
        l = 1
    if l == 'B':
        l = 2
    c[i] = (x, l)

c.sort()
#print(c)
res = [0, 0, 0]
psq = 0
for i in range(n):
    k = c[i]
    sq = k[0] * k[0]
    res[k[1]] += sq - psq + (4 * sq)
    psq = sq

print("R -", res[0], file=fout)
print("G -", res[1], file=fout)
print("B -", res[2], file=fout)


fin.close()
fout.close()