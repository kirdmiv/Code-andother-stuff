fin = open("cards.in", 'r')
fout = open("cards.out", 'w')

n = int(fin.readline().rstrip())
crds = list(fin.readline().rstrip())

i = 1
while i < n:
    if crds[i] != crds[i-1]:
        break
    i += 1

j = n - 2
while j >= 0:
    if crds[j] != crds[j+1]:
        break
    j -= 1

c = (i + n - j - 1) // 2
r = 0
b = 0
max1 = max2 = 0
maxr= maxb = 0
for k in range(i, j+1):
    if crds[k] == 'R':
        r += 1
        maxr += 1
        maxb = 0

    if crds[k] == 'B':
        b += 1
        maxb += 1
        maxr = 0

#    print(maxb, maxr, k, max1, max2)
    if maxb > max1 and crds[k] != crds[k+1]:
        max2 = max1
        max1 = maxb
    elif maxb > max2 and crds[k] != crds[k+1]:
        max2 = maxb

    if maxr > max1 and crds[k] != crds[k+1]:
        max2 = max1
        max1 = maxr
    elif maxr > max2 and crds[k] != crds[k+1]:
        max2 = maxr

if crds[0] != crds[-1]:
    print(r + b - max1 - max2, file=fout)
else:
    if crds[0] == 'R':
        print(min(b, i + r, n - j - 1 + r), file=fout)
    else:
        print(min(r, i + b, n - j - 1 + b), file=fout)
fin.close()
fout.close()
