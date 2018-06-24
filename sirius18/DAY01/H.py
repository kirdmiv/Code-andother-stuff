import math

def smt():
    sq = math.sqrt(n)
    d = []
    s = 1
    while s <= sq:
        if s == sq:
            d.append(s)
        elif n % s == 0:
            d.append(s)
            d.append(n // s)
        s += 1
    return sorted(d)


def nod(a, b):
    while a % b != 0:
        a %= b
        a, b = max(a, b), min(a, b)
    return b
n = int(input())

d = smt()
cnt = 0
for i in range(len(d)):
    for j in range(i+1, len(d)):
        if d[i] * d[j] > n:
            break
        if nod(d[j], d[i]) == 1:
            cnt += 1
print(cnt)