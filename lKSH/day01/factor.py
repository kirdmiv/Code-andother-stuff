def factor(n):
    per_n = n
    res = []
    i = 2
    while i * i <= per_n:
        while n % i == 0:
            res.append(str(i))
            n //= i
        i += 1
    if not res:
        res.append(str(per_n))
    elif n != 1:
        res.append(str(n))
    return res


divs = factor(int(input()))
print(' '.join(divs))
