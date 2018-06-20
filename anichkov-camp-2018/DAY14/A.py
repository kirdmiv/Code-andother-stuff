import math

fin = open("bb8.in", 'r')
fout = open("bb8.out", 'w')

a, b, h, w = map(int, fin.readline().split())
print(math.ceil(h / a)* math.ceil(w / b), file=fout)
fin.close()
fout.close()
