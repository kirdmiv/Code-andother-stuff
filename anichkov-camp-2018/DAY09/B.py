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



fin = open("vectors.in", 'r')
fout = open("vectors.out", 'w')

x1, y1, x2, y2 = map(int, fin.readline().split())
x3, y3, x4, y4 = map(int, fin.readline().split())

v1 = Point(x1, y1)
v2 = Point(x2, y2)
v12 = v2.substr(v1)

v3 = Point(x3, y3)
v4 = Point(x4, y4)
v34 = v4.substr(v3)

print(v12.length(), v34.length(), file=fout)
print(*v12.sum_result(v34), file=fout)
print(v12.scalar(v34), v12.vectr(v34), file=fout)
print(abs(0.5 * v12.vectr(v34)), file=fout)

fin.close()
fout.close()
