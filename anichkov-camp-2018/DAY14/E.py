import math

fin = open("encryption.in", 'r')
fout = open("encryption.out", 'w')

lol = [0, 9, 189, 2889, 38889, 488889, 5888889, 68888889, 788888889, 8888888889, 98888888889, 1088888888889,
       11888888888889, 128888888888889, 1388888888888889, 14888888888888889, 158888888888888889, 1688888888888888889,
       17888888888888888889]
l, r = map(int, fin.readline().split())
len_l = 0
len_r = 0
f = False
for i in range(len(lol)):
    if lol[i] >= l and not f:
        len_l = i
        f = True
    if lol[i] >= r:
        len_r = i
        break
# 123456789101112131
# 41516171819202122
# print(len_l, len_r)
l -= lol[len_l - 1] + 1
r -= lol[len_r - 1]
# print(l, r)
l = math.ceil(l / len_l)
r = math.floor(r / len_r)
l += 10 ** (len_l - 1)
r += 10 ** (len_r - 1)
print(l, r)
print(r - l, file=fout)

fin.close()
fout.close()
