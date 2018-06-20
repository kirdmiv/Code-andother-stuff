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


twotri_in = open('twotri.in', 'r')
twotri_out = open('twotri.out', 'w')

points = []
xa1, ya1, xb1, yb1, xc1, yc1 = map(int, twotri_in.readline().split())
xa2, ya2, xb2, yb2, xc2, yc2 = map(int, twotri_in.readline().split())
points.append(point(xa1, ya1))
points.append(point(xb1, yb1))
points.append(point(xc1, yc1))
points.append(point(xa2, ya2))
points.append(point(xb2, yb2))
points.append(point(xc2, yc2))
twotri_in.close()

ans1 = [0, 0, 0]
for i in range(3):
    v0 = points[(i + 2) % 3]
    tmp = points[i].substr(v0)
    res = tmp.angle(points[(i + 1) % 3].substr(v0))
    ans1[i] = abs(res)

ans2 = [0, 0, 0]
for i in range(3, 6):
    v0 = points[(i + 2) % 3 + 3]
    tmp = points[i].substr(v0)
    res = tmp.angle(points[(i + 1) % 3 + 3].substr(v0))
    ans2[i - 3] = abs(res)

ans1.sort()
ans2.sort()

if ans1[0] == ans2[0] and ans1[1] == ans2[1] and ans1[2] == ans2[2]:
    print("YES", file=twotri_out)
else:
    print("NO", file=twotri_out)
