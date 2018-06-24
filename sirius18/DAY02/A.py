n = int(input())
a = list(map(int, input().split()))

if n == 2 and a[0] >= a[1]:
    print("YES")
elif n == 2:
    print("NO")

if n == 3 and a[0] >= a[1] >= a[2]:
    print("YES")
elif n == 3:
    print("NO")

if n == 3 and (a[0] >= a[1] >= a[2] >= a[3] or a[3] >= a[1] >= a[2] >= a[0]):
    print("YES")
elif n == 3:
    print("NO")

if n > 7:
