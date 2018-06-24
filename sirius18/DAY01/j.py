n = int(input())
s = []
for i in range(n):
    n, f, o, d, t = input().split()
    o = int(o)
    d = int(d)
    t = int(t)
    s.append((-(o+d+t)/3, i, n, f))
s.sort()
for i in range(len(s)):
    print(s[i][2], s[i][3])