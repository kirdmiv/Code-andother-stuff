import math

INF = 10 ** 9 + 7


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #Вычитание векторов
    def substr(self, other):
        return Point(self.x - other.x, self.y - other.y)

    #Расстояние между двумя точками
    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    #Длина вектора
    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    #Скалярное произведение векторов
    def scalar(self, other):
        return self.x * other.x + self.y * other.y

    #Векторное произведение векторов
    def vectr(self, other):
        return self.x * other.y - self.y * other.x

    #Угол между 2мя вкторами
    def angle(self, other):
        return math.atan2(self.vectr(other), self.scalar(other))

    #Полярный угол точки
    def polar_angle(self):
        return math.atan2(self.y, self.x)

    #Прямая по двум точкам
    def line(self, other):
        A = other.y - self.y
        B = self.x - other.y
        C = -A * self.x - B * self.y
        return A, B, C

    #Сумма 2х векторов
    def sum_result(self, other):
        return self.x + other.x, self.y + other.y

    #Увеличение вектора в k раз
    def kmult(self, k):
        self.x *= k
        self.y *= k

    #Нормализация вектора
    def normalize(self):
        k = math.sqrt(self.x ** 2 + self.y ** 2)
        self.x /= k
        self.y /= k

    #Возвращает перпендикулярный вектор
    def perp(self):
        return Point(-self.y, self.x)



fin = open("basicvector.in", 'r')
fout = open("basicvector.out", 'w')

x1, y1 = map(int, fin.readline().split())
x2, y2 = map(int, fin.readline().split())
n = int(fin.readline().rstrip())

v1 = Point(x1, y1)
v2 = Point(x2, y2)
v2 = v2.substr(v1)

print(v2.x, v2.y, file=fout)
v2.normalize()
print(v2.x, v2.y, file=fout)
v2.kmult(n)
print(v2.x, v2.y, file=fout)
v1 = Point(x1, y1)
v2 = Point(x2, y2)
v2 = v2.substr(v1)
print(v2.y, -v2.x, file=fout)
print(-v2.y, v2.x, file=fout)
fin.close()
fout.close()
