import math

a, b = map(int, input().split())

cnt = 0
k = str(a)
g = 0    
for j in range(len(k)):
    g += int(k[j])
if (g % 2 == 0):
    cnt += 1
    #cnt += math.ceil((b-a)/2)
k = str(b)
s = 0    
for j in range(len(k)):
    s += int(k[j])
if (s % 2 == 0):
    
    cnt += 1
    #if (cnt == 1):
    #    cnt += (b-a)//2

if (g % 2 == 0 and s % 2 == 0):
    cnt += (b-a-1)//2
elif (g % 2  == 0 and s % 2 == 1):
    cnt += (b-a)//2
elif (g % 2  == 1 and s % 2 == 0):
    cnt += (b-a)//2
elif (g % 2  == 1 and s % 2 == 1):
    cnt += (b-a+1)//2

print(cnt)