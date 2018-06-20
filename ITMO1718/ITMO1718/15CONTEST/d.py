n, p = map(int, input().split())

s = [0] * n
s[0] = 0
for i in range(1, n):
    s[i] = (s[i-1] + (p%(i+1))) % (i+1)
print(s[n-1] + 1)