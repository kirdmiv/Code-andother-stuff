MAX_SEC = 86400


watches_in = open('watches.in', 'r')
watches_out = open('watches.out', 'w')

# Читаем
n = int(watches_in.readline())
watches = []
for i in range(n):
    hours, mins, seconds = map(int, watches_in.readline().split(':'))
    tmp = ((hours * 60) + mins) * 60 + seconds
    watches.append(tmp)
watches_in.close()

res = []
cnt = 0
start = 0
b = True
for i in range(len(watches)):
    cnt += scanline[i][1]
    if cnt != 0 and b:
        start = scanline[i][0]
        b = False
    if cnt == 0:
        res.append([start, scanline[i][0]])
        start = 0
        b = True

print(len(res), file=watches_out)
for i in range(len(res)):
    print(*res[i], file=watches_out)
watches_out.close()
