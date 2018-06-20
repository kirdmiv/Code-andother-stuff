transfers_in = open('transfers.in', 'r')
transfers_out = open('transfers.out', 'w')

# Читаем
a, b, c, d = map(int, transfers_in.readline().split())
transfers_in.close()

first_bus = sorted([a, b])
second_bus = sorted([c, d])

scanline = [[first_bus[0], -1], [first_bus[1], 1], [second_bus[0], -1], [second_bus[1], 1]]
scanline.sort()
ans = 0
cnt = 0
for i in range(4):
    cnt += scanline[i][1]
    if cnt == -2:
        ans = scanline[i + 1][0] - scanline[i][0] + 1
print(ans, file=transfers_out)
transfers_out.close()
