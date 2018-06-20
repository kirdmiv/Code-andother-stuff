timetable_in = open('timetable.in', 'r')
timetable_out = open('timetable.out', 'w')

# Читаем
n = int(timetable_in.readline())
scanline = [[-1, -1, -1]]
for i in range(n):
    tmp = list(map(int, timetable_in.readline().split()))
    scanline.append([tmp[0], tmp[1], i])
scanline.sort()
timetable_in.close()

res = []
ans = 0
start = 0
finish = scanline[0][1]
ind = 0

for i in range(1, n + 1):
    if scanline[ind][1] <= scanline[i][0]:
        res.append(scanline[i][2] + 1)
        ind = i
    else:
        if scanline[ind][1] > scanline[i][1]:
            res.pop()
            res.append(scanline[i][2] + 1)
            ind = i
print(*res, file=timetable_out)
timetable_out.close()
