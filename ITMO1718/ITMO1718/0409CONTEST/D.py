prostoe_navernoe = 1267650600228229401496703205361

ps = [1] * 10000
for i in range(1, 10000):
    ps[i] = (ps[i - 1] * 131) % prostoe_navernoe

n = int(input())
hhhhashhhhhes = [[] for i in range(n)]
for i in range(n):
    s = input()
    hash = [0] * (len(s) + 1)
    hash[1] = ord(s[0])
    for i in range(2, len(s) + 1):
        hash[i] = (hash[i - 1] + ord(s[i - 1]) * ps[i - 1]) % prostoe_navernoe
    hhhhashhhhhes[i] = hash

l = 0
r = min(len(hhhhashhhhhes[0]), len(hhhhashhhhhes[1])) + 1
while r - l > 1:
    m = (r + l) // 2











n = int(input())
for i in range(n):
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
