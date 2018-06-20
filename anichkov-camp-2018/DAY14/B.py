fin = open("numbers.in", 'r')
fout = open("numbers.out", 'w')

n, m = fin.readline().split()
if int(n) > int(m):
    print(0, file=fout)
    exit()
if int(n) == int(m):
    print(1, file=fout)
    exit()
res1 = m[len(m)-len(n):]
res2 = m[:len(m)-len(n)]
if res2 == '':
    res2 = '0'
if int(res1) >= int(n):
    print(int(res2)+1, file=fout)
else:
    print(res2, file=fout)
fin.close()
fout.close()
