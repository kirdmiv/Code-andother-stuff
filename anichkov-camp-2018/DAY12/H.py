import math

def gayron(a, b, c):
    p = (a+b+c)/2
    return math.sqrt(p*(p-a)*(p-b)*(p-c))

a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())
a3, b3, c3 = map(int, input().split())

res = gayron(a1, b1, c1) + gayron(a2, b2, c2) + gayron(a3, b3, c3)

print(math.sqrt(res/6))