def sieve(a, b):
    res = [True] * (b + 1)
    res[0] = res[1] = False
    i = 2
    while i * i <= b:
        for j in range(i * i, b + 1, i):
            res[j] = False
        i += 1
    return res


a, b = tuple(map(int, input().split()))
res = sieve(a, b)
ans = ''
for i in range(len(res)):
    if i >= a:
        if res[i]:
            ans += str(i) + ' '
print(ans)
