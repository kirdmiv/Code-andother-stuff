n = int(input())
a = list(map(int, input().split()))

pref = [0] * n
pref[0] = a[0]
pref2 = [0] * n

for i in range(1, n):
    pref[i] = pref[i-1] + a[i]

c = pref[-1] // 3

p1 = 0
p2 = 0
#print(pref)

cnt =0
    
    
#print(pref2, c , pref)
for i in range(1, n-1):
    if pref[i-1] == c:
            cnt += 1
    if pref[i] == 2*c:
        p2 += cnt    

print(p2)