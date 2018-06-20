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
    return matrix[n - 1][m - 1]


turtle_in = open('turtle.in', 'r')
turtle_out = open('turtle.out', 'w')

n, m = map(int, turtle_in.readline().split())
lst = []
for i in range(n):
    lst.append(list(map(int, turtle_in.readline().split())))
print(turtle(lst, n, m), file=turtle_out)
turtle_in.close()
turtle_out.close()
