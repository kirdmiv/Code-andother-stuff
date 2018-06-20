def u(x):
    s = a[x]
    for i in g[x]:
        tmp = a[i] + s
        if tmp > INF:
            a[i] = tmp - INF
        else:
            a[i] = tmp

INF = 10 ** 9 + 7
n = int(input())
a = list(map(int, input().split()))
g = [[] for i in range(n)]
for i in range(n - 1):
    x, y = map(int, input().split())
    g[x - 1].append(y - 1)
    g[y - 1].append(x - 1)
m = int(input())
for i in range(m):
    t, v = map(int, input().split())
    if t == 1:
        u(v - 1)
    else:
        print(a[v - 1])

'''
4
1 1 1 1
1 2
1 3
2 4
9
2 1
2 2
2 3
2 4
1 1
2 1
2 2
2 3
2 4


'''

'''
2
1 1
1 2
14
2 2
2 1
1 1
2 2
1 2
2 1
1 1
2 2
1 2
2 1
1 1
2 2
1 2
2 1
'''