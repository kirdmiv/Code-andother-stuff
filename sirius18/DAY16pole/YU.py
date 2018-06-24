n = int(input())
f = 2*n+1
a=['.' for i in range(f)]
l = r = f//2

for i in range(n):
    a[l] = '*'
    a[r] = '*'
    print(*a, sep='')
    l-=1
    r+=1