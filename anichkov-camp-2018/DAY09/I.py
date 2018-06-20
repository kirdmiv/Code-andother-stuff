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


fin = open("area.in", 'r')
fout = open("area.out", 'w')

n = int(fin.readline())

points = []
for i in range(n):
    x, y = map(float, fin.readline().split())
    points.append(Point(x, y))
fin.close()

sq = 0
for i in range(0, n):
    v1 = points[i]
    v2 = points[(i+1)%n]
    sq += (v1.x - v2.x) * (v1.y + v2.y)
print(abs(sq)/2, file=fout)

fin.close()
fout.close()
