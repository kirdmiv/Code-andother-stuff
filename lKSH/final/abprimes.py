def sieve(a, b):
    res = [True] * (b + 1)
    res[0] = res[1] = False
    i = 2
    while i * i <= b:
        for j in range(i * i, b + 1, i):
            res[j] = False
        i += 1
    return res


res = sieve(0, 100000)
ans = [0] * 100001
for i in range(1, len(res)):
    if res[i]:
        ans[i] = ans[i - 1] + 1
    else:
        ans[i] = ans[i - 1]

abprimes_in = open('abprimes.in', 'r')
abprimes_out = open('abprimes.out', 'w')

n = int(abprimes_in.readline())
lst = []
for i in range(n):
    lst.append(list(map(int, abprimes_in.readline().split())))
abprimes_in.close()

for i in lst:
    j, k = i[0], i[1]
    print(ans[k] - ans[j - 1], file=abprimes_out)
abprimes_out.close()
