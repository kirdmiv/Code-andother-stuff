def gcd(a, b):
    while a * b != 0:
        if a < b:
            a, b = b, a
        a, b = a % b, b
    return a + b
    
    
a, b = map(int, input().split())
minus = False
if a < 0:
    minus = True
    a = abs(a)
gcd = gcd(a, b)
a = a // gcd
b = b // gcd
if minus:
    a = 0 - a
print(a, b)
