queen_in = open('queen.in', 'r')
queen_out = open('queen.out', 'w')

# Читаем
n, m = map(int, queen_in.readline().split())
x, y = map(int, queen_in.readline().split())
queen_in.close()

ans = n + m - 2
ans += min(n - x, m - y)
ans += min(x - 1, m - y)
ans += min(n - x, y - 1)
ans += min(x - 1, y - 1)

print(ans, file=queen_out)
queen_out.close()
