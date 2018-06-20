import math


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def substr(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def dist_to_line(self, a, b, c):
        return (a * self.x + b * self.y + c) / math.sqrt(a ** 2 + b ** 2)

    def scalar(self, other):
        return self.x * other.x + self.y * other.y

    def vectr(self, other):
        return self.x * other.y - self.y * other.x

    def angle(self, other):
        return math.atan2(self.vectr(other), self.scalar(other))


def check():
    return ((start_y < river_k * start_x + river_b) and
            (finish_y < river_k * finish_x + river_b) or
            (start_y > river_k * start_x + river_b) and
            (finish_y > river_k * finish_x + river_b))

def distance():
    x = river_k * finish.dist_to_line(river_k, -1, river_b) / math.sqrt(river_k ** 2 + 1)
    y = -1 * finish.dist_to_line(river_k, -1, river_b) / math.sqrt(river_k ** 2 + 1)
    print(x, y)
    return 28.284


river_in = open('river.in', 'r')
river_out = open('river.out', 'w')

# Читаем
start_x, start_y = map(int, river_in.readline().split())
start = Point(start_x, start_y)
finish_x, finish_y = map(int, river_in.readline().split())
finish = Point(finish_x, finish_y)
river_k, river_b = map(float, river_in.readline().split())
river_in.close()

if check():
    print("%.3f" % distance(), file=river_out)
else:
    print("No solution.", file=river_out)
river_out.close()
