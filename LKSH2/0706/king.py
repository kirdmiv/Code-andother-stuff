def king(lst):
    matrix = [[0] * 9 for i in range(9)]
    matrix[0][0] = 0
    for i in range(1, 9):
        matrix[i][0] = INF
    for j in range(1, 9):
        matrix[0][j] = INF
    for i in range(1, 9):
        for j in range(1, 9):
            matrix[i][j] = min(matrix[i][j - 1], matrix[i - 1][j], matrix[i - 1][j - 1]) + lst[i - 1][j - 1]
    path = []
    k = 8
    j = 8
    while k > 0 or j > 0:
        path.append(LETTERS[j - 1] + str(k))
        prev = min(matrix[k][j - 1], matrix[k - 1][j], matrix[k - 1][j - 1])
        if matrix[k][j - 1] == prev:
            j -= 1
        elif matrix[k - 1][j] == prev:
            k -= 1
        else:
            j, k = j - 1, k - 1
    path.reverse()
    return matrix[8][8], path


INF = 10 ** 9 + 7
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

king_in = open('king2.in', 'r')
king_out = open('king2.out', 'w')

lst = []
for i in range(8):
    lst.append(list(map(int, king_in.readline().split())))
lst.reverse()
king_in.close()
ans, way = king(lst)
print(ans, file=king_out)
print(*way, file=king_out)
king_out.close()
