fin = open("skates.in", 'r')
fout = open("skates.out", 'w')

m = int(fin.readline().rstrip())
a2 = list(map(int, fin.readline().split()))
n = int(fin.readline().rstrip())
a1 = list(map(int, fin.readline().split()))

a1.sort()
a2.sort()

i = 0
j = 0
cnt = 0
while i < n:
    while j < m:
        if a2[j] >= a1[i]:
            cnt += 1
            j += 1
            break
        j += 1
    i += 1

print(cnt, file=fout)

fin.close()
fout.close()
