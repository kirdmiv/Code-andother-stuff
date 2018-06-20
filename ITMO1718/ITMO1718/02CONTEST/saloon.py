INF = 10 ** 9

fin = open("saloon.in", 'r')
fout = open("saloon.out", 'w')

n = int(fin.readline())
lst = [[] for i in range(n)]
ans = [0 for i in range(n + 1)]
for i in range(n):
    mins, secs, deg = map(int, fin.readline().split())
    time = mins * 60 + secs
    lst[i] = [time, deg]

ans[0] = lst[0][0]
queue = 0
tmpque = 0
for i in range(n):
    if lst[i][0] != INF:
        queue += 1
        tmpque = queue
        for j in range(i + 1, n):
            if lst[j][0] != INF and lst[j][0] < lst[j - 1][0] + 20:
                if lst[j][1] >= tmpque:
                    tmpque += 1
                else:
                    ans[j + 1] = lst[j][0]
                    lst[j][0] = INF
            else:
                queue -= 1
                break
        res = i
        for k in range(i - 1, -1, -1):
            if lst[k][0] != INF:
                res = k
                break
        ans[i + 1] = max(ans[res + 1], lst[i][0]) + 20

for i in range(1, n + 1):
    print(ans[i] // 60, ans[i] % 60, file=fout)
fout.close()
fin.close()
