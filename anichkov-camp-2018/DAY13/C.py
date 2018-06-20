fin = open("castle.in", 'r')
fout = open("castle.out", 'w')

n = int(fin.readline())
l = 0
r = 1000000000000000001
while r - l > 1:
    m = (r + l) // 2
    if m*(m+1)/2 <= n:
        l = m
    else:
        r = m
print(l, file=fout)
fin.close()
fout.close()