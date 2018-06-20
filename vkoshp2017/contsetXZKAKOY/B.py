a, b, c = map(int, input().split())
r = 0
l = 1
n = 1
if a == 1 or b == 1 or c == 1:
    l = 0
if a == b == c == 0:
    r = 1
print(r, l, n)