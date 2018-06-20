n, m = map(int, input().split())
lst = [[0 for i in range(m)] for j in range(n)]
lst[0] = [1 for i in range(m)]
for i in range(n):
    lst[i][0] = 1
for i in range(1, n):
    for j in range(1, m):
        lst[i][j] = lst[i-1][j] + lst[i][j-1]
for i in lst:
    print(*i)
