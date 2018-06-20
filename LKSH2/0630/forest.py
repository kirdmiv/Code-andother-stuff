import math


def distance(a1, b1, a2, b2):
    return math.sqrt((a1 - a2) ** 2 + (b1 - b2) ** 2)


def time(x):
    return distance(0, 1, x, a) / vp + distance(x, a, 1, 0) / vf


def tern_search():
    left = -1
    right = 2
    for i in range(100):
        x0 = (right - left) / 3 + left
        x1 = 2 * (right - left) / 3 + left
        if time(x0) < time(x1):
            right = x1
        else:
            left = x0
    return min(left, right)


forest_in = open('forest.in', 'r')
forest_out = open('forest.out', 'w')

# Читаем
vp, vf = map(int, forest_in.readline().split())
a = float(forest_in.readline())
forest_in.close()

print(tern_search(), file=forest_out)
forest_out.close()
