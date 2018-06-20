fin = open("apples.in", 'r')
fout = open("apples.out", 'w')

n, s = map(int, fin.readline().split())
a = []
for i in range(n):
    ai, bi = map(int, fin.readline().split())
    if ai - bi == 0:
        a.append((0, ai, bi, i + 1))
    elif ai - bi < 0:
        a.append((-1, ai, bi*(-1), i + 1))
    else:
        a.append((1, ai*(-1), bi*(-1), i + 1))
a.sort()
ans = []
for i in range(n):
    if a[i][0] == 0:
        if s <= a[i][1]:
            print(-1, file=fout)
            exit()
        else:
            ans.append(a[i][3])
    elif a[i][0] == -1:
        if s <= a[i][1]:
            print(-1, file=fout)
            exit()
        else:
            s = s - a[i][1] - a[i][2]
            ans.append(a[i][3])
    else:
        if s <= -a[i][1]:
            print(-1, file=fout)
            exit()
        else:
            s = s + a[i][1] - a[i][2]
            ans.append(a[i][3])
print(*ans, file=fout)
fin.close()
fout.close()