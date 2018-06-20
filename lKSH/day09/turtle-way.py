def turtle(lst, n, m):
    matrix = [[0] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                matrix[0][0] = lst[0][0]
            elif i > 0 and j > 0:
                matrix[i][j] = min(matrix[i - 1][j], matrix[i][j - 1]) + lst[i][j]
            elif j == 0:
                matrix[i][0] = matrix[i - 1][0] + lst[i][0]
            elif i == 0:
                matrix[0][j] = matrix[0][j - 1] + lst[0][j]
    path = []
    k = n - 1
    j = m - 1
    path.append((n, m))
    while k > 0 or j > 0:
        if matrix[k - 1][j] < matrix[k][j - 1]:
            path.append((k, j + 1))
            k -= 1
        else:
            path.append((k + 1, j))
            j -= 1
    path.reverse()
    return matrix[n - 1][m - 1], path


turtle_in = open('turtle-way.in', 'r')
turtle_out = open('turtle-way.out', 'w')

n, m = map(int, turtle_in.readline().split())
lst = []
for i in range(n):
    lst.append(list(map(int, turtle_in.readline().split())))
turtle_in.close()
ans, way = turtle(lst, n, m)
print(ans, file=turtle_out)
for i in way:
    print(*i, file=turtle_out)
turtle_out.close()
