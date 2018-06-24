n = int(input())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))

f = True
for i in range(0, n):
    if f:
        print(400-i, end=' ')
    else:
        print(n-i, end=' ')
    if a1[i] == 1:
        f = False
print()
f = True
for i in range(0, n):
    if f:
        print(400-i, end=' ')
    else:
        print(n-i, end=' ')
    if a2[i] == 1:
        f = False

    