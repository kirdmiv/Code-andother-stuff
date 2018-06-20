fin = open("travel.in", "r")
fout = open("travel.out", "w")

def sisya(a):
    m = a[0][0]
    mi = 0
    print(a)
    for i in range(1, len(a)):
        if a[i][0] < m:
            m = a[i][0]
            mi = i
    return a[mi][1]



def check(x, y):
    p = ""
    s_p = ""
    c_p = ""
    a = (s_x - x)
    b = (s_y - y)
    s = (abs(a) + abs(b))
    print(a, b, x, y, s_x, s_y)
    if a > 0:
        p += "W" * a
    else:
        p += "E" * -a
    if b > 0:
        p += "N" * b
    else:
        p += "S" * -b
    s_p = p
    rsadjkgf = 0
    if x > 0:
        if g[y][x - 1] == 'T':
            p += "WE" * ((n - 1) // 2)
            if (n - 1) // 2 < (n - 1) / 2:
                p += "W"
                rsadjkgf = 1
            return len(p), p
        else:
            c_p = s_p + "WE" * (n - 1)
    if x < w - 1:
        if g[y][x + 1] == 'T':
            print(y, x, (n - 1) // 2, p)
            p += "EW" * ((n - 1) // 2)
            print(p)
            if (n - 1) // 2 < (n - 1) / 2:
                p += "E"
                rsadjkgf = 1
            print(y, x, (n - 1) // 2, p)

            return len(p), p
        else:
            c_p = s_p + "EW" * (n - 1)
    if y > 0:
        if g[y - 1][x] == 'T':
            p += "NS" * ((n - 1) // 2)
            if (n - 1) // 2 < (n - 1) / 2:
                p += "N"
                rsadjkgf = 1
            return len(p), p
        else:
            c_p = s_p + "NS" * (n - 1)
    if y < h - 1:
        if g[y + 1][x] == 'T':
            p += "SN" * ((n - 1) // 2)
            if (n - 1) // 2 < (n - 1) / 2:
                p += "S"
                rsadjkgf = 1
            return len(p), p
        else:
            c_p = s_p + "SN" * (n - 1)
    return len(c_p), c_p


w, h, n = map(int, fin.readline().split())
g = [[]] * h

s_x = 0
s_y = 0

for i in range(h):
    t = list(fin.readline().rstrip())
    if not(s_x):
        for j in range(len(t)):
            if t[j] == 'V':
                s_x = j
                s_y = i
    g[i] = t

res = []
print(g)
for i in range(h):
    for j in range(w):
        if g[i][j] == 'T':
            res.append(check(j, i))

print(sisya(res), file=fout)

fin.close()
fout.close()