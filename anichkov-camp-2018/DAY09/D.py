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
        B = self.x - other.x
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



fin = open("distance1.in", 'r')
fout = open("distance1.out", 'w')

x3, y3 = map(int, fin.readline().split())
x1, y1 = map(int, fin.readline().split())
x2, y2 = map(int, fin.readline().split())

p1 = Point(x1, y1)
p2 = Point(x2, y2)
p3 = Point(x3, y3)

A, B, C = p1.line(p2)
d = abs((A*x3 + B*y3 + C) / math.sqrt(A * A + B * B))
print(d, file=fout)
v13 = p3.substr(p1)
v12 = p2.substr(p1)
flag = False
if v13.scalar(v12) < 0:
    print(v13.length(), file=fout)
    flag = True
else:
    print(d, file=fout)

v23 = p3.substr(p2)
v21 = p1.substr(p2)
if flag:
    print(v13.length(), file=fout)
elif v23.scalar(v21) < 0:
    print(v23.length(), file=fout)
else:
    print(d, file=fout)

fin.close()
fout.close()
