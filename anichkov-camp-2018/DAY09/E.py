import math

INF = 10 ** 9 + 7


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Вычитание векторов
    def substr(self, other):
        return Point(self.x - other.x, self.y - other.y)

    # Расстояние между двумя точками
    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    # Длина вектора
    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    # Скалярное произведение векторов
    def scalar(self, other):
        return self.x * other.x + self.y * other.y

    # Векторное произведение векторов
    def vectr(self, other):
        return self.x * other.y - self.y * other.x

    # Угол между 2мя вкторами
    def angle(self, other):
        return math.atan2(self.vectr(other), self.scalar(other))

    # Полярный угол точки
    def polar_angle(self):
        return math.atan2(self.y, self.x)

    # Прямая по двум точкам
    def line(self, other):
        A = other.y - self.y
        B = self.x - other.x
        C = -A * self.x - B * self.y
        return A, B, C

    # Сумма 2х векторов
    def sum_result(self, other):
        return self.x + other.x, self.y + other.y

    # Увеличение вектора в k раз
    def kmult(self, k):
        self.x *= k
        self.y *= k

    # Нормализация вектора
    def normalize(self):
        k = math.sqrt(self.x ** 2 + self.y ** 2)
        self.x /= k
        self.y /= k

    # Возвращает перпендикулярный вектор
    def perp(self):
        return Point(-self.y, self.x)


def pereseka():
    A1, B1, C1 = p1.line(p2)
    A2, B2, C2 = p3.line(p4)
    d = A1 * B2 - B1 * A2
    d1 = -C1 * B2 + C2 * B1
    d2 = -A1 * C2 + C1 * A2

    if (A1 * A1 + B1 * B1) == 0 and (A2 * A2 + B2 * B2) == 0:
        if x1 == x2 == x3 == x4 and y1 == y2 == y3 == y4:
            return True
        else:
            return False
    if d == d1 == d2 == 0:
        if min(x3, x4) <= x1 <= max(x3, x4) and min(y3, y4) <= y1 <= max(y3, y4) or \
                min(x3, x4) <= x2 <= max(x3, x4) and min(y3, y4) <= y2 <= max(y3, y4) or \
                min(x1, x2) <= x3 <= max(x1, x2) and min(y1, y2) <= y3 <= max(y1, y1) or \
                min(x1, x2) <= x4 <= max(x1, x2) and min(y1, y2) <= y4 <= max(y1, y2):
            return True
        else:
            return False
    elif d == 0:
        return False
    else:
        x0 = d1 / d
        y0 = d2 / d
        if min(x3, x4) <= x0 <= max(x3, x4) and min(y3, y4) <= y0 <= max(y3, y4) and \
                min(x1, x2) <= x0 <= max(x1, x2) and min(y1, y2) <= y0 <= max(y1, y2):
            return True
        else:
            return False
    '''
    v31 = p1.substr(p3)
    v32 = p2.substr(p3)
    if v31.vectr(v32) < 0:
        print("NO", file=fout)
        exit()

    v41 = p1.substr(p4)
    v42 = p2.substr(p4)
    if v42.vectr(v41) < 0:
        print("NO", file=fout)
        exit()

    v13 = p3.substr(p1)
    v14 = p4.substr(p1)
    if v14.vectr(v13) < 0:
        print("NO", file=fout)
        exit()


    v23 = p3.substr(p2)
    v24 = p4.substr(p2)
    if v23.vectr(v24) < 0:
        print("NO", file=fout)
        exit()

    print("YES", file=fout)
    '''


fin = open("distance2.in", 'r')
fout = open("distance2.out", 'w')

x1, y1, x2, y2 = map(int, fin.readline().split())
x3, y3, x4, y4 = map(int, fin.readline().split())

p1 = Point(x1, y1)
p2 = Point(x2, y2)
p3 = Point(x3, y3)
p4 = Point(x4, y4)

if pereseka():
    print(0, file=fout)
    exit()

dist = []
A, B, C = p1.line(p2)
if x1 == x2 and y1 == y2:
    pass
d = abs((A * x3 + B * y3 + C) / math.sqrt(A * A + B * B))
v13 = p3.substr(p1)
v12 = p2.substr(p1)
v23 = p3.substr(p2)
v21 = p1.substr(p2)
if v13.scalar(v12) < 0:
    dist.append(v13.length())
elif v23.scalar(v21) < 0:
    dist.append(v23.length())
else:
    dist.append(d)

d = abs((A * x4 + B * y4 + C) / math.sqrt(A * A + B * B))
v14 = p4.substr(p1)
v24 = p4.substr(p2)
if v14.scalar(v12) < 0:
    dist.append(v14.length())
elif v24.scalar(v21) < 0:
    dist.append(v24.length())
else:
    dist.append(d)

A, B, C = p3.line(p4)
d = abs((A * x1 + B * y1 + C) / math.sqrt(A * A + B * B))
v31 = p1.substr(p3)
v34 = p4.substr(p3)
v41 = p1.substr(p4)
v43 = p3.substr(p4)
if v31.scalar(v34) < 0:
    dist.append(v31.length())
elif v41.scalar(v43) < 0:
    dist.append(v41.length())
else:
    dist.append(d)

d = abs((A * x2 + B * y2 + C) / math.sqrt(A * A + B * B))
v32 = p2.substr(p3)
v42 = p2.substr(p4)
if v32.scalar(v34) < 0:
    dist.append(v32.length())
elif v42.scalar(v43) < 0:
    dist.append(v42.length())
else:
    dist.append(d)

print(min(dist), file=fout)
fin.close()
fout.close()
