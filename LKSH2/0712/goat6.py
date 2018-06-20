import math

INF = 10 ** 9 + 7


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def substr(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def scalar(self, other):
        return self.x * other.x + self.y * other.y

    def vectr(self, other):
        return self.x * other.y - self.y * other.x

    def angle(self, other):
        return math.atan2(self.vectr(other), self.scalar(other))


trees = []
goat_in = open('goat6.in', 'r')
goat_out = open('goat6.out', 'w')
n = int(goat_in.readline())
for i in range(n):
    x, y = map(float, goat_in.readline().split())
    trees.append(Point(x, y))

dist = [INF] * n
for i in range(n):
    for j in range(n):
        if i != j:
            dist[i] = min(dist[i], trees[i].dist(trees[j]))

ans = -1
for i in range(n):
    for j in range(n):
        if i != j:
            ans = max(ans, (math.pi * (max(dist[i], dist[j]) ** 2)) +
                      (math.pi * min((min(dist[j], dist[i]), trees[i].dist(trees[j]) - (max(dist[i], dist[j])) ** 2))))
            print(i, j, ans)

print(ans)
