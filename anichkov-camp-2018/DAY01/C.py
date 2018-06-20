fin = open("points.in", 'r')
fout = open("points.out", 'w')

w1, h1, w2, h2 = map(int, fin.readline().split())
r1 = (w1-1) * (h1- 1)
r2 = (w2+1) * (h2+ 1)

print(max(0, r1-r2), file=fout)

fin.close()
fout.close()