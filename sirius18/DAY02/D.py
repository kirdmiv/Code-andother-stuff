import math


def bsearch(x):
    l = 0
    r = len(dels)
    while r - l > 1:
        m = (l+ r) // 2
        if dels[m][0] <= x:
            l = m
        else:
            r = m
    return l


def smt(x, y):
    #print(x, y)
    sq = math.sqrt(x)
    d = []
    s = 1
    while s <= sq:
        #print(x, y, s)
        if s == sq and s > y and dels[bsearch(s)][0] == s:
            dels[bsearch(s)][1] += 1
        elif x % s == 0:
            if s > y and dels[bsearch(s)][0] == s:
                dels[bsearch(s)][1] += 1
            #print(bsearch(s), bsearch(x // s), s, x)
            if x // s > y and dels[bsearch(x // s)][0] == x // s:
                dels[bsearch(x // s)][1] += 1
        s += 1
    return d


def smt2(x, y):
    #print(x, y)
    sq = math.sqrt(x)
    d = []
    s = 1
    while s <= sq:
        if s == sq and s > y:
            d.append([s, 1])
        elif x % s == 0:
            if s > y:
                d.append([s, 1])
            if x // s > y:
                d.append([x // s, 1])
        s += 1
    return sorted(d)



n = int(input())
dels = []
x, y = map(int, input().split())
dels = smt2(x-y, y)
for i in range(n-1):
    x, y = map(int, input().split())
    smt(x-y, y)

ans = []
for i in dels:
    if i[1] == n:
        ans.append(i[0])

#print(dels)
print(len(ans))
print(*ans)