Lnum = list(map(int, input().split()))
Lstr = list(map(str, input().split()))
n = len(Lnum)
Lright = [0 for i in range(n)]
for i in range(0, n):
    tmp = Lnum.index(i)
    Lright[tmp] = Lstr[i]
for i in Lright:
    print(i, end=' ')
