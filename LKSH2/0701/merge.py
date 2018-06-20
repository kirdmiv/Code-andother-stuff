merge_in = open('merge.in', 'r')
merge_out = open('merge.out', 'w')

# Читаем
n = int(merge_in.readline())
scanline = []
for i in range(n):
    tmp = list(map(int, merge_in.readline().split()))
    scanline.append([tmp[0], -1])
    scanline.append([tmp[1], 1])
scanline.sort()
merge_in.close()

res = []
cnt = 0
start = 0
b = True
for i in range(len(scanline)):
    cnt += scanline[i][1]
    if cnt != 0 and b:
        start = scanline[i][0]
        b = False
    if cnt == 0:
        res.append([start, scanline[i][0]])
        start = 0
        b = True

print(len(res), file=merge_out)
for i in range(len(res)):
    print(*res[i], file=merge_out)
merge_out.close()
