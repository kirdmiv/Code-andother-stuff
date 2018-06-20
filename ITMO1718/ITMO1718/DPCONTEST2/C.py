INF = 10 ** 9 + 7

n = int(input())
a = list(map(int, input().split()))


for i in range(n - 1):
    l = len(a)
    d = [10001] * l
    mind = INF
    minin = -1
    for j in range(l - 1):
        if abs(a[j] - a[j + 1]) < mind:
            mind = abs(a[j] - a[j + 1])
            minin = j
    a = a[:minin] + [(a[minin] + a[minin + 1]) / 2] + a[minin+2:]
    print(a)



    p
    2p + 1
    3p + 2