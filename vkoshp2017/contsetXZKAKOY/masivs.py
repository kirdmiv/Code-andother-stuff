import math
zalupen = open("nasik.txt", "w")
pisundra = [0] * 2000
for i in range(1, 2000):
    res = 0
    for j in range(1, i + 1):
        for k in range(1, j + 1):
            x = math.sqrt(i * i + j * j + k * k)
            if int(x) == x:
                res += 1
    pisundra[i] = pisundra[i - 1] + res
    print(i)
print(pisundra, file=zalupen)
zalupen.close()