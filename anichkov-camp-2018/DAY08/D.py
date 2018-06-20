fin = open("sequence.in", 'r')
fout = open("sequence.out", 'w')

n = int(fin.readline().rstrip())
a = list(map(int, fin.readline().split()))
a.sort(reverse=True)
s = sum(a)
if s % 2 != 0:
    print(-1, file=fout)
    exit()
nuzn = s // 2
print("", file=fout)
fin.close()
fout.close()
