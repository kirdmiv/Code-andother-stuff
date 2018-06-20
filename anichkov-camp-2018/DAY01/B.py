import math

EPS = 10 ** -7

def dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


fin = open("twotri.in", 'r')
fout = open("twotri.out", 'w')

x1, y1, x2, y2, x3, y3 = map(int, fin.readline().split())
x4, y4, x5, y5, x6, y6 = map(int, fin.readline().split())
l1 = dist(x1, y1, x2, y2)
l2 = dist(x3, y3, x2, y2)
l3 = dist(x1, y1, x3, y3)

l4 = dist(x4, y4, x5, y5)
l5 = dist(x6, y6, x5, y5)
l6 = dist(x4, y4, x6, y6)

ls1 = [l1, l2, l3]
ls1.sort()

ls2 = [l4, l5, l6]
ls2.sort()

#print(ls1, ls2)
if abs(((ls1[0] / ls2[0]) - (ls1[1] / ls2[1]))) < EPS and abs(((ls1[2] / ls2[2]) - (ls1[1] / ls2[1]))) < EPS\
        and abs(((ls1[2] / ls2[2]) - (ls1[1] / ls2[1]))) < EPS:
    print("YES", file=fout)
    exit()
print("NO", file=fout)

fin.close()
fout.close()