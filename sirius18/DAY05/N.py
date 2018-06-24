import math
n = int(input())
if n > 5.625 * 1e17 and n < 6.25 * 1e17:
    print(2)
else:
    n-=1
    cnt = 0
    while n > 0:
        n-=2 ** int(math.log2(n))
        cnt += 1
    print(cnt%3)