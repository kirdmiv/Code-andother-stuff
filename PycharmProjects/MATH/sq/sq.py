import math

a, b, c = map(int, input().split())
d = b * b - (4 * a * c)
print("Finding D... D={}".format(d))
if d < 0:
    print("Shit... no solutions :(")
else:
    sqd = math.sqrt(d)
    x1 = (-b + sqd) / (2 * a)
    x2 = (-b - sqd) / (2 * a)
    print("x1, x2 = {}, {}".format(x1, x2))
    print("{} +- {} / {}".format(-b, sqd, 2*a))
    print("{} +- sqrt({}) / {}".format(-b, d, 2 * a))
