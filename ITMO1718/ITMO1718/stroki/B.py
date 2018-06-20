fin = open("trans.in", 'r')
fout = open("trans.out", 'w')

n = int(fin.readline().rstrip())
z = list(map(int, fin.readline().split()))
p = [0] * n
for i in range(1, n):
    j = z[i]
    k = 1
    while j > 0:
        p[i + k - 1] = max(p[i + k - 1], k)
        j -= 1
        k += 1

print(*p, file=fout)
fin.close()
fout.close()
