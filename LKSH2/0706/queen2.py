queen_in = open('queen2.in', 'r')
queen_out = open('queen2.out', 'w')

# Читаем
n = int(queen_in.readline())
queen_in.close()
strings = [False] * n
diagonals1 = [False] * n
diagonals2 = [False] * n

for i in range(n):


print(ans, file=queen_out)
queen_out.close()
