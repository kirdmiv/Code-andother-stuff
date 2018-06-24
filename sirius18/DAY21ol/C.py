n = int(input())
a = [[0] * 100 for i in range(100)]
for i in range(n):
    s = input()
    ord1 = ord(s[0]) - ord('a')
    ord2 = -1
    cnt1 = 1
    cnt2 = 0
    f = True
    for j in range(1, len(s)):
        ind = ord(s[j]) - ord('a')
        #print(ind)
        if (ind == ord1):
            cnt1 += 1
        elif (ord2 == -1):
            ord2 = ind
            cnt2 += 1
        elif(ind == ord2):
            cnt2 += 1
        else:
            f = False
    if f:
        if (ord2 == -1):
            for i in range(100):
                a[ord1][i] += cnt1
                if i != ord1:
                    a[i][ord1] += cnt1
        else:
            a[ord1][ord2] += (cnt1 + cnt2) 
            a[ord2][ord1] += (cnt1 + cnt2)
            
mx = [0] * 100
for i in range(100):
    mx[i] = max(a[i])

#for i in a:
#    print(*i)
print(max(mx))