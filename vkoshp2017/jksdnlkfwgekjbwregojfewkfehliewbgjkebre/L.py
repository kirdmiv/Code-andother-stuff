a, b, c = map(int, input().split())
if a + b < c:
    print("Impossible")
else:
    if a >= c:
        print(c, 0)
    elif b >= c:
        print(0, c)
    elif c - a <= b:
        print(a, c - a)
    elif c - b<= a:
        print(c - b, b)