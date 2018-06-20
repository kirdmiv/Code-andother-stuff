n =int(input())
a = []
for i in range(n):
    tmp = list(input())
    a.append(tmp)

cnt = 0
for i in range(n):
    for j in range(n):
        if a[i][j] == 'C':
            cnt += 1

r = cnt // 2
for i in range(n):
    for j in range(n):
        if r > 0:
            print(1, end='')
        else:
            print(2, end='')
        if a[i][j] == 'C':
            r -= 1
    print()
