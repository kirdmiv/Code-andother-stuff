x1, y1, x2, y2, x3, y3 = map(int, input().split())
x1 -= x3
x2 -= x3
y1 -= y3
y2 -= y3
print(abs(x1 * y2 - x2 * y1)/2)