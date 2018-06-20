n = int(input())
a = list(map(int, input().split()))
flag = False
for i in range(len(a)):
    if a[i] == 1:
        print(i + 1, i + 1)
        exit()
print(-1)