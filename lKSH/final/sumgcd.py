def sumgcd(n):
    for i in range(2, n):
        if n / i == n // i:
            return n // i, n - n // i
    return 1, n - 1


sumgcd_in = open('sumgcd.in', 'r')
sumgcd_out = open('sumgcd.out', 'w')

n = int(sumgcd_in.readline())
ans = sumgcd(n)
print(*ans, file=sumgcd_out)
sumgcd_in.close()
sumgcd_out.close()
