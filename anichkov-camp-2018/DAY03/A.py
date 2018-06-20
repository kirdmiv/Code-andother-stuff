fin = open("setdiff.in", 'r')
fout = open("setdiff.out", 'w')

n = int(fin.readline().rstrip())
a1 = list(map(int, fin.readline().split()))
m = int(fin.readline().rstrip())
a2 = list(map(int, fin.readline().split()))


i = 0
j = 0
while i < n:
    flag = False
    while j < m:
        if a2[j] == a1[i]:
            flag = True
            break
        if a2[j] > a1[i]:
            break
        j += 1
    if not flag:
        print(a1[i], end=" ", file=fout)
    i += 1


fin.close()
fout.close()
