import math


class point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def substr(self, other):
        return point(self.x - other.x, self.y - other.y)

    def angle(self, other):
        y = self.x * other.y - self.y * other.x
        x = self.x * other.x + self.y * other.y
        return math.atan2(y, x)


goat_in = open('goat1.in', 'r')
goat_out = open('goat1.out', 'w')

points = []
for i in range(3):
    x, y = map(int, goat_in.readline().split())
    points.append(point(x, y))
goat_in.close()

ans = [0, 0, 0]
for i in range(3):
    v0 = points[(i + 2) % 3]
    curpoint = points[i]
    tmp = points[i].substr(v0)
    res = tmp.angle(points[(i + 1) % 3].substr(v0))
    ans[i] = abs((res * 180) / math.pi)
    points[i] = curpoint

print(max(ans), file=goat_out)
