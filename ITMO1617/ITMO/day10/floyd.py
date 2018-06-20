n = int(input())
lst = []
for i in range(n):
    tmp = list(map(int, input().split()))
    lst.append(tmp)
for k in range(n):
    for i in range(n):
        for j in range(n):
            lst[i][j] = min(lst[i][j], lst[i][k] + lst[k][j])
for i in lst:
    print(*i)
