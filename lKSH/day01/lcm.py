def gcd(a, b):
    while a * b != 0:
        if b > a:
            a, b = b, a
        a, b = a % b, b
    return a + b


def lcm(a, b):
    res = a * b // gcd(a, b)
    return res


a, b = tuple(map(int, input().split()))
print(lcm(a, b))
