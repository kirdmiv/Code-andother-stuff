prostoe_navernoe = 4294967291

s = input()
hash = [0] * (len(s) + 1)
ps = [1] * len(s)
for i in range(1, len(s)):
    ps[i] = (ps[i - 1] * 131) % prostoe_navernoe
p = 131
hash[1] = ord(s[0])
for i in range(2, len(s) + 1):
    hash[i] = (hash[i - 1] + ord(s[i - 1]) * ps[i - 1]) % prostoe_navernoe

while True:
    pass