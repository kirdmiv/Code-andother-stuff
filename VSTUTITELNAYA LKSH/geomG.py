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


n = int(input())

points = []
for i in range(n):
    x, y = map(float, input().split())
    points.append(point(x, y))


ans = "YES"
f1 = False
f2 = False
for i in range(n):
    v0 = points[(i + 1) % n]
    tmp = points[i].substr(v0)
    tmp_angle = tmp.vectr(points[(i + 2) % n].substr(v0))
    if tmp_angle < 0:
        f1 = True
        if f2:
            ans = "NO"
            break
    if tmp_angle > 0:
        f2 = True
        if f1:
            ans = "NO"
            break

print(ans)