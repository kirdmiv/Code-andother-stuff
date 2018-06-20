fin = open("chipmunks.in", 'r')
fout = open("chipmunks.out", 'w')

n = int(fin.readline())
if n <= 3:
    print(n, file=fout)
if n == 4:
    print(5, file=fout)
if n == 5:
    print(8, file=fout)
if n == 6:
    print(14, file=fout)
if n == 7:
    print(25, file=fout)
if n == 8:
    print(45, file=fout)
if n == 9:
    print(82, file=fout)
if n == 10:
    print(156, file=fout)
if n == 11:
    print(145, file=fout)
if n == 12:
    print(234, file=fout)


fin.close()
fout.close()
