n = input()
k = int(input())

a = [0] * 27
for i in n:
    tmp = ord(i) - 97
    a[tmp] += 1

a.sort(reverse=True)


facts = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800, 479001600, 6227020800, 87178291200, 1307674368000, 20922789888000, 355687428096000, 6402373705728000, 121645100408832000, 2432902008176640000, 51090942171709440000, 1124000727777607680000, 25852016738884976640000, 620448401733239439360000, 15511210043330985984000000, 403291461126605635584000000]


res = 0
i = 0
c = 0
c_n = a[0]
while k > 0:
    if a[i] == c_n:
        c += 1
    else:
        c = 1
        c_n = a[i]
    res += a[i]
    k-=1
    i += 1
    if a[i] == 0:
        i -= 1
        break


s_i = a[i]
res2 = 1
st_i = i

while i < 26:
    i += 1
    if a[i] == s_i:
        res2 += 1

i = st_i
while i > 0:
    i -= 1
    if a[i] == s_i:
        res2 += 1


res2 = facts[res2] // (facts[c] * (facts[res2 - c]))

print(res, res2)