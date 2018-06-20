def knight(lst, n, m):
    matrix = [[0] * m for i in range(n)]
    matrix[0][0] = lst[0][0]
    for i in range(1, n):
        for j in range(1, m):
            if i > 1 and j > 1:
                res1 = matrix[i - 2][j - 1]
                res2 = matrix[i - 1][j - 2]
                if res1 != 0 and res2 != 0:
                    matrix[i][j] = max(res1, res2) + lst[i][j]
            elif j == 1 and i > 1:
                res = matrix[i - 2][0]
                if res != 0:
                    matrix[i][1] = res + lst[i][1]
            elif i == 1 and j > 1:
                res = matrix[0][j - 2]
                if res != 0:
                    matrix[1][j] = res + lst[1][j]
    ans = matrix[n - 1][m - 1]
    if ans != 0:
        return ans
    return -1


knight_in = open('knight.in', 'r')
knight_out = open('knight.out', 'w')

n, m = map(int, knight_in.readline().split())
lst = []
for i in range(n):
    lst.append(list(map(int, knight_in.readline().split())))
print(knight(lst, n, m), file=knight_out)
knight_in.close()
knight_out.close()
