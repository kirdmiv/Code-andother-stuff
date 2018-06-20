import math
arr1 = [2,5,6,8,23,8,34,43,96,23,74,45,246,8]
arr = [3,8,6,4,2,5,9,0,7,1]
n = len(arr)
l = int(math.log2(n))
st = [[0] * n for i in range(l)]
st[0] = arr
for k in range(1, l):
    for i in range(n - 2 ** (k-1)):
        st[k][i] = min(st[k - 1][i], st[k - 1][i + 2 ** (k-1)])
print(*st, sep="\n")

while True:
    i, j = map(int, input().split())
    k = int(math.log2(j-i+1))
    print(min(st[k][i], st[k][j-2**k+1]))