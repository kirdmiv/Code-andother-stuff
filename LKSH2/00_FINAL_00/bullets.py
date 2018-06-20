import math

EPS = 10 ** -9


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def substr_1(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def substr(self, x, y):
        return Point(self.x - x, self.y - y)

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def scalar(self, other):
        return self.x * other.x + self.y * other.y

    def vectr(self, other):
        return self.x * other.y - self.y * other.x

    def angle(self, other):
        return math.atan2(self.vectr(other), self.scalar(other))

    def dist(self, a, b, c):
        return (a * x + b * y + c) / math.sqrt(a ** 2 + b ** 2)

    def dist_dot(self, dot):
        return math.sqrt((self.x - dot.x) ** 2 + (self.y - dot.y) ** 2)


bullets_in = open('bullets.in', 'r')
bullets_out = open('bullets.out', 'w')

points = []
n, m = map(int, bullets_in.readline().split())
for i in range(n):
    x, y = map(int, bullets_in.readline().split())
    points.append(Point(x, y))

ans = [0] * m

for i in range(m):
    x, y, r, vx, vy = map(int, bullets_in.readline().split())
    a = vy
    b = -vx
    c = -(a * x + b * y)
    res = 0
    circle = Point(x, y)
    dot = Point(vx, vy)
    v2 = dot
    for j in range(n):
        v0 = points[j].substr_1(circle)
        if v0.scalar(v2) < 0:
            if circle.dist_dot(points[j]) <= r:
                res += 1
        else:
            if abs(points[j].dist(a, b, c)) <= r:
                res += 1
    ans[i] = res

print(*ans, file=bullets_out)
bullets_in.close()
