import math

goat_in = open('goat2.in', 'r')
goat_out = open('goat2.out', 'w')

length, rope = map(int, goat_in.readline().split())

if rope < length / 2:
    square_rope = rope ** 2
    res = math.pi * (square_rope)
elif math.sqrt(2 * ((length / 2) ** 2)) < rope:
    res = length ** 2
else:
    d = length / 2
    square_rope = rope ** 2
    res = math.pi * (square_rope)
    res -= 4 * (square_rope * math.acos(d / rope) - d
                * math.sqrt(square_rope - (d ** 2)))

print(res, file=goat_out)
