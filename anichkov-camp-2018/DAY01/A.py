fin = open("subarray.in", 'r')
fout = open("subarray.out", 'w')


n = fin.readline()
lst = list(map(int, fin.readline().split()))
m = int(fin.readline())
for i in range(m):
    i, j = map(int, fin.readline().split())
    i -= 1
    print(*lst[i:j], file=fout)

fin.close()
fout.close()