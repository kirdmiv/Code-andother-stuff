def getBin(x):
    res = ""
    cnt = 0
    while x > 0:
        d = x % 2
        if d == 1:
            cnt += 1
        res += str(d)
        x //= 2
    return res, cnt

a, b, c = map(int, input().split())
print(getBin(a), getBin(b), getBin(c))