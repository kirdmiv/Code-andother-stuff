n = int(input())
ans = 0
l = 1
r = 1
curl =1
cur = 0
for i in range(1, n+1):
    m = int(input())    
    cur += m
    if cur < 0:
        curl = i+1
        cur = 0
    if cur >= ans:
        l = curl
        r = i+1
        ans = cur + m
        cur = 0
    if m > ans:
        l = max(i+1, curl)
        r = i+1
        ans = m
        cur = 0
print(l, r)