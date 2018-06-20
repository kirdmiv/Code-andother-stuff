queen_in = open('queen1.in', 'r')
queen_out = open('queen1.out', 'w')

# Читаем
m, n = map(int, queen_in.readline().split())
queen_in.close()
field = [[False] * m for i in range(n)]

for i in range(n - 1, -1, -1):
    for j in range(m - 1, -1, -1):
        if (not field[i][j]) and (i != 0 or j != 0):
            field[i] = [True] * m
            for k in range(i - 1, -1, -1):
                field[k][j] = True
                if abs(j + k - i) < m:
                    field[k][j + k - i] = True
            break
field[-1][-1] = True

ans = 2
if field[0][0]:
    ans = 1
print(ans, file=queen_out)
queen_out.close()
