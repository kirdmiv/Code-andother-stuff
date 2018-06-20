def divis(d):
    i = 1
    L = []
    while i ** 2 < d:
        if d % i ==0:
            d = d // i
            L.append(i)
        L.append(d)
        i += 1
    return L



a, b, c, d, e, f = tuple(map(int, input().split()))
res = a * c * e
res2 = b * d * f
print(divis())