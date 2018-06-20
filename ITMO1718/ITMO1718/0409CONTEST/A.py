prostoe_navernoe = 1267650600228229401496703205361

s = input()
hash = [0] * (len(s) + 1)
ps = [1] * len(s)
for i in range(1, len(s)):
    ps[i] = (ps[i - 1] * 131) % prostoe_navernoe
p = 131
hash[1] = ord(s[0])
for i in range(2, len(s) + 1):
    hash[i] = (hash[i - 1] + ord(s[i - 1]) * ps[i - 1]) % prostoe_navernoe
m = int(input())
for i in range(m):
    a, b, c, d, = map(int, input().split())
    r1 = hash[b] - hash[a - 1]
    r2 = hash[d] - hash[c - 1]
    #print(r1, r2)
    if r1 < 0:
        r1 += prostoe_navernoe
    if r2 < 0:
        r2 += prostoe_navernoe
    if a < c:
        r1 *= ps[c - a]
        r1 %= prostoe_navernoe
    elif c < a:
        r2 *= ps[a - c]
        r2 %= prostoe_navernoe
    if b - a == d - c and r1 == r2:
        print("Yes")
    else:
        print("No")
