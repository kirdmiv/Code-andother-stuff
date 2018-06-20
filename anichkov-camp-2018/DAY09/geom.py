import math

INF = 10 ** 9 + 7


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Вектор по началу и концу
    def substr(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    # Расстояние между двумя точками
    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    # Полярный угол точки
    def polar_angle(self):
        return math.atan2(self.y, self.x)

    # Прямая по двум точкам
    def line(self, other):
        A = other.y - self.y
        B = self.x - other.x
        C = -A * self.x - B * self.y
        return Line(A, B, C)

    # Расстояние до прямой
    def dist_to_line(self, line):
        return abs((line.a * self.x + self.y * line.b + line.c) / math.sqrt(line.a * line.a + line.b * line.b))

    # Расстояние до луча
    def dist_to_luch(self, p1, p2):
        v13 = self.substr(p1)
        v12 = p2.substr(p1)
        if v13.scalar(v12) < 0:
            return v13.length()
        else:
            return self.dist_to_line(p1.line(p2))

    def dist_to_otrezok(self, p1, p2):
        v13 = self.substr(p1)
        v12 = p2.substr(p1)
        v23 = self.substr(p2)
        v21 = p1.substr(p2)
        if v13.scalar(v12) < 0:
            return v13.length()
        elif v23.scalar(v21) < 0:
            return v23.length()
        else:
            return self.dist_to_line(p1.line(p2))


class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Длина вектора
    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    # Скалярное произведение векторов
    def scalar(self, other):
        return self.x * other.x + self.y * other.y

    # Векторное произведение векторов
    def vectr(self, other):
        return self.x * other.y - self.y * other.x

    # Угол между 2мя вкторами
    def angle(self, other):
        return math.atan2(self.vectr(other), self.scalar(other))

    # Сумма 2х векторов
    def sum_result(self, other):
        return self.x + other.x, self.y + other.y

    # Увеличение вектора в k раз
    def kmult(self, k):
        self.x *= k
        self.y *= k

    # Нормализация вектора
    def normalize(self):
        k = math.sqrt(self.x * self.x + self.y * self.y)
        self.x /= k
        self.y /= k

    # Возвращает перпендикулярный вектор
    def perpYX(self):
        return Vector(-self.y, self.x)

    # Возвращает перпендикулярный вектор
    def perpXY(self):
        return Vector(self.y, -self.x)

    def tri_sq(self, other):
        return self.vectr(other) / 2


class Line():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # Напрвляющий вектор прямой
    def naprav(self):
        return Vector(-self.b, self.a)

    # Возвращает перпендикулярную прямую
    def perp(self):
        return Line(-self.b, self.a, 0)

    def perpVector(self):
        return Vector(self.a, self.b)

    def parall(self, d):
        slon = math.sqrt(self.a * self.a + self.b * self.b)
        return Line(self.a, self.b, self.c + d * slon), Line(self.a, self.b, self.c - d * slon)
