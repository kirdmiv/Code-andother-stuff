rect_in = open('rect.in', 'r')
rect_out = open('rect.out', 'w')

INF = 10 ** 9 + 1

# Читаем
n = int(rect_in.readline())
left_x = -INF
top_y = -INF
right_x = INF
bottom_ = INF

for i in range(n):
    x1, y1, x2, y2 = map(int, rect_in.readline().split())
    right_x = min(right_x, x2)
    bottom_ = min(bottom_, y2)
    left_x = max(left_x, x1)
    top_y = max(top_y, y1)
rect_in.close()

if right_x < left_x or bottom_ < top_y:
    print(-1, file=rect_out)
else:
    print(left_x, top_y, right_x, bottom_, file=rect_out)

rect_out.close()
