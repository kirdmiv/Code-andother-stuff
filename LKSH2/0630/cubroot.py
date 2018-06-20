def solution(x):
    return a * x ** 3 + b * x ** 2 + c * x + d


def bin_solution(mid):
    return a * solution(mid) <= 0


def bin_search():
    left = -1
    right = 1
    while solution(left) * solution(right) > 0:
        left *= 2
        right *= 2
    for i in range(100):
        mid = (right + left) / 2
        if bin_solution(mid):
            left = mid
        else:
            right = mid
    return left


cubroot_in = open('cubroot.in', 'r')
cubroot_out = open('cubroot.out', 'w')

# Читаем
a, b, c, d = map(int, cubroot_in.readline().split())

print(bin_search(), file=cubroot_out)
cubroot_in.close()
cubroot_out.close()
