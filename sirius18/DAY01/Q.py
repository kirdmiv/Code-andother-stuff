import math


def nod(a, b):
    while a % b != 0:
        a %= b
        a, b = max(a, b), min(a, b)
    return b


n = int(input())
a = list(map(int, input().split()))

st = [[0] * n for i in range(int(math.log2(n)))]
for i in range(n):
    st[0][i] = a[i]
for i in range(1, int(math.log2(n))+1):
    for j in range(n-2**i+1):
        print(i, j)
        st[i][j] = nod(st[i-1][j], st[i-1][j+int(2**(i-1))])

print(st)
k = int(input())
for i in range(k):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    k = int(math.log2(r-l+1))
    print(nod(st[k][l], st[k][r-2**k+1]), end=' ')