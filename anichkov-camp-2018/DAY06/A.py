fin = open("m2e.in", 'r')
fout = open("m2e.out", 'w')

n = int(fin.readline().rstrip())
for i in range(n):
    a = list(map(int, fin.readline().split()))
    for j in range(i):
        if a[j] == 1:
            print(i+1, j+1, file=fout)
fin.close()
fout.close()
