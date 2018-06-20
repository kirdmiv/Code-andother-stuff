fin = open("request.in", 'r')
fout = open("request.out", 'w')

n = int(fin.readline().rstrip())
a =[]
for i in range(n):
    s, f= map(int, fin.readline().split())
    a.append((f, s))
a.sort()
last_f = 0
cnt = 0
for i in range(n):
    if a[i][1] >= last_f:
        cnt += 1
        last_f = a[i][0]
print(cnt, file=fout)
fin.close()
fout.close()
