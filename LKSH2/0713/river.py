import math

INF = 10 ** 6


def check():
    return ((start_y < river_k * start_x + river_b) and
            (finish_y < river_k * finish_x + river_b) or
            (start_y > river_k * start_x + river_b) and
            (finish_y > river_k * finish_x + river_b))


def distance(a1, b1, a2, b2):
    return math.sqrt((a1 - a2) ** 2 + (b1 - b2) ** 2)


def tern_solution(x):
    y = river_k * x + river_b
    dist1 = distance(start_x, start_y, x, y)
    dist2 = distance(finish_x, finish_y, x, y)
    return dist1 + dist2


def tern_search():
    left = -INF
    right = INF
    for i in range(100):
        x0 = ((right - left) / 3) + left
        x1 = (2 * (right - left) / 3) + left
        if tern_solution(x0) < tern_solution(x1):
            right = x1
        else:
            left = x0
    return tern_solution(min(left, right))


river_in = open('river.in', 'r')
river_out = open('river.out', 'w')

# Читаем
start_x, start_y = map(int, river_in.readline().split())
finish_x, finish_y = map(int, river_in.readline().split())
river_k, river_b = map(float, river_in.readline().split())
river_in.close()

if check():
    print("%.3f" % tern_search(), file=river_out)
else:
    print("No solution.", file=river_out)
river_out.close()
