a, b, c, d, e, f = map(int, input().split())
if c == 0 and d != 0:
    print('Ron')
elif b == 0 or d == 0:
    print('Hermione')
elif a == 0:
    print('Ron')
elif f == 0:
    print('Hermione')
elif a == 0 or c == 0 or e == 0:
    print('Ron')
else:
    start_sand = a * c * e
    res = start_sand / a * b / c * d / e * f
    if start_sand < res:
        print('Ron')
    else:
        print('Hermione')
