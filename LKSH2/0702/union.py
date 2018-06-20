union_in = open('union.in', 'r')
union_out = open('union.out', 'w')

vertical = []
horizontal = []

# Читаем
n = int(union_in.readline())
for i in range(n):
    x1, y1, x2, y2 = map(int, union_in.readline().split())
    vertical.append((x1, 0, y1, y2))
    vertical.append((x2, 1, y1, y2))
    horizontal.append((y1, 0, x1, x2))
    horizontal.append((y2, 1, x1, x2))
union_in.close()

vertical.sort()
horizontal.sort()

ans = 0
for i in range(2 * n - 1):
    res = 0
    left = 0
    balance = 0
    for j in range(2 * n):
        if vertical[j][2] <= horizontal[i][0] and vertical[j][3] >= horizontal[i + 1][0]:
            if vertical[j][1] == 0:
                balance += 1
                if balance == 1:
                    left = vertical[j][0]
            else:
                balance -= 1
                if balance == 0:
                    res += vertical[j][0] - left
    ans += res * (horizontal[i + 1][0] - horizontal[i][0])

print(ans, file=union_out)
union_out.close()
