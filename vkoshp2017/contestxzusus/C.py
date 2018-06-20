import math

def dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))


fin = open("dog3.in", "r")
fout = open("dog3.out", "w")
x1, y1 = map(int, fin.readline().split())
x2, y2 = map(int, fin.readline().split())
x3, y3 = map(int, fin.readline().split())
dist1 = dist(x1, y1, x2, y2)
dist2 = dist(x2, y2, x3, y3)
dist3 = dist(x1, y1, x3, y3)
dists = [dist1, dist2, dist3]


pesina1 = min(dist1, dist3)
repesina1 = max(dist3 - pesina1, dist1 - pesina1)
resusina1 = math.pi * (pesina1 * pesina1 + repesina1 * repesina1)

pesina2 = min(dist2, dist1)
repesina2 = max(dist1 - pesina2, dist2 - pesina2)
resusina2 = math.pi * (pesina2 * pesina2 + repesina2 * repesina2)


pesina3 = min(dist2, dist3)
repesina3 = max(dist3 - pesina3, dist2 - pesina3)
resusina3 = math.pi * (pesina3 * pesina3 + repesina3 * repesina3)

ansus = max(resusina1, resusina2, resusina3)
print(ansus, file=fout)
fin.close()
fout.close()
