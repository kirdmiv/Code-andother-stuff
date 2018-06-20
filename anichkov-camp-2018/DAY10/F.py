def square(a1):
    a2 = [[0] * 4 for i in range(4)]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                a2[i][j] += a1[i][k] * a1[k][j]
            a2[i][j] %= 2
    return a2


a_gen = [[0] * 4 for i in range(4)]


def gen(k1):
    if k1 == 16:
        if square(a_gen) == a:
            return a_gen
        return False
    a_gen[k1 // 4][k1 % 4] = 0
    r = gen(k1 + 1)
    if r:
        return r
    a_gen[k1 // 4][k1 % 4] = 1
    r = gen(k1 + 1)
    if r:
        return r
    return False


fin = open('sqroot.in', 'r')
fout = open('sqroot.out', 'w')

# Читаем

a = [[]] * 4
for i in range(4):
    a[i] = list(map(int, fin.readline().split()))

ans = False

res = []
g = gen(0)

if g:
    for i in g:
        print(*i, file=fout)
else:
    print("NO SOLUTION", file=fout)
fin.close()
fout.close()
