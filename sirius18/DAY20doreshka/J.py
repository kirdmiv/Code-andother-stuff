s = input()
i =0
c = ""
while s[i] != "=":
    c += s[i]
    i += 1
    #print(i)
n = int(c)
i += 1
a = []
while (i < len(s)):
    c = ""
    while i < len(s) and s[i] != "+":
        c += s[i]
        i += 1
    i += 1
    a.append(int(c))
    #print(i)

a.reverse()
#print(a)
if (len(a) == 1):
    print("No solution")
else:
    if(a[1]+1 <= a[0]-1):
        a[0] -= 1
        a[1] += 1
        a.reverse()
        while (a[-1] - a[-2]) >= a[-2]:
            a.append(a[-1] - a[-2])
            a[-2] = a[-3]
    else:
        a[1] += a[0]
        a.pop(0)
        a.reverse()    
    last = a.pop()
    print(n, '=', sep='', end='')
    for i in a:
        print(i, '+', sep='', end='')
    print(last)