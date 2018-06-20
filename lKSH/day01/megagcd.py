def gcd(a, b):
    while a * b != 0:
        if b > a:
            a, b = b, a
        a, b = a % b, b
    return a + b


def megagcd(lst):
    for i in range(len(lst) - 1):
        lst[i + 1] = gcd(lst[i], lst[i + 1])
    return lst[-1]


lst = list(map(int, input().split()))
res = megagcd(lst)
print(res)
