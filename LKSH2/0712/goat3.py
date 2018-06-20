import math


class point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def substr(self, other):
        return point(self.x - other.x, self.y - other.y)

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def scalar(self, other):
        return self.x * other.x + self.y * other.y

    def vectr(self, other):
        return self.x * other.y - self.y * other.x

    def angle(self, other):
        return math.atan2(self.vectr(other), self.scalar(other))


goat_in = open('goat3.in', 'r')
goat_out = open('goat3.out', 'w')

x1, y1, x2, y2 = map(int, goat_in.readline().split())
x3, y3, length = map(int, goat_in.readline().split())

vectA = point(x1, y1)
vectB = point(x2, y2)
vectC = point(x3, y3)

goat_in.close()

vectAC = vectC.substr(vectA)
vectAB = vectB.substr(vectA)
vectBA = vectA.substr(vectB)
vectBC = vectC.substr(vectB)

if vectAC.scalar(vectAB) < 0:
    min_distance = vectAC.length()
    max_distance = vectBC.length()

elif vectBC.scalar(vectBA) < 0:
    min_distance = vectBC.length()
    max_distance = vectAC.length()

else:
    vectCA = vectA.substr(vectC)
    vectCB = vectB.substr(vectC)

    if vectAB.length() == 0:
        min_distance = vectCA.length()
    else:
        min_distance = abs(vectCA.vectr(vectCB) / vectAB.length())
    max_distance = max(vectCA.length(), vectCB.length())

print(max(0, min_distance - length), file=goat_out)
print(max(0, max_distance - length), file=goat_out)
