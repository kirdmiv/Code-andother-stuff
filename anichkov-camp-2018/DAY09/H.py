import math


class point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def substr(self, other):
        return point(self.x - other.x, self.y - other.y)

    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def scalar(self, other):
        return self.x * other.x + self.y * other.y

    def vectr(self, other):
        return self.x * other.y - self.y * other.x

    def angle(self, other):
        return math.atan2(self.vectr(other), self.scalar(other))


ngon_in = open('polygon.in', 'r')
ngon_out = open('polygon.out', 'w')

n = int(ngon_in.readline())

points = []
for i in range(n):
    x, y = map(float, ngon_in.readline().split())
    points.append(point(x, y))
ngon_in.close()

ans = "YES"
length = points[0].dist(points[1])
angle = math.pi * (n - 2) / n

v0 = points[1]
tmp = points[0].substr(v0)
tmp_angle = tmp.angle(points[2].substr(v0))

if tmp_angle == -angle:
    angle = -angle

for i in range(n):
    v0 = points[(i + 1) % n]
    tmp = points[i].substr(v0)
    tmp_angle = tmp.vectr(points[(i + 2) % n].substr(v0))
    if tmp_angle < 0:
        ans = "NO"
        break

print(ans, file=ngon_out)
ngon_out.close()
