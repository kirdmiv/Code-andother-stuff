def check(n, k):
    r1 = n // k
    r2 = n - (k * (n // k))
    n2 = n - r2
    ans = 0
    r3 = 0
    while n2 > 0:
        ans += (r3 * r1)
        r3 += r1
        n2 -= r1
    ad = n - r1 - 1
    while r2 > 0:
        r2 -= 1
        ans += ad - r2
    return ans

t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    print(check(n, k))