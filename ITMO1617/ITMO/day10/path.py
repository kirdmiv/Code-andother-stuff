def floyd(lst):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                lst[i][j] = min(lst[i][j], lst[i][k] + lst[k][j])
    return lst


n = int(input())
lst = []
for i in range(n):
    tmp = list(map(int, input().split()))
    lst.append(tmp)
ans = 0
lst = floyd(lst)
for i in range(n):
    for j in range(n):
        res = max(lst[i][j], lst[j][i])
        if res > ans:
            ans = res
print(ans)
