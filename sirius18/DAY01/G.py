s = list(input())
d = int(s[0]+s[1])
m = int(s[2]+s[3])
y = int(s[4]+s[5]+s[6]+s[7])

y-=1
d += (y * 365)
d += (y // 4)
d -= (y // 100)
d += (y // 400)
y+=1

if m > 1:
    d += 31
if m > 2:
    d += 28
    if y % 400 == 0 or (y%4==0 and y%100!=0):
        d+=1
if m > 3:
    d += 31
if m > 4:
    d += 30
if m > 5:
    d += 31
if m > 6:
    d += 30
if m > 7:
    d += 31
if m > 8:
    d += 31
if m > 9:
    d += 30
if m > 10:
    d += 31
if m > 11:
    d += 30
print(d)


