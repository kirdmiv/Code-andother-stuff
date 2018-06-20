def hodga(n):
    matrix = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                matrix[0][0] = 1
            elif i > 0 and j > 0:
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
            elif j == 0:
                matrix[i][0] = matrix[i - 1][0]
            elif i == 0:
                matrix[0][j] = matrix[0][j - 1]
    matrix[0][0] = 0
    return matrix


def horse(n):
    matrix = [[0] * n for i in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if i == n - 1 and j == n - 1:
                matrix[n - 1][n - 1] = 1
            elif i < n - 1 and j < n - 1:
                matrix[i][j] = matrix[i + 1][j] + matrix[i][j + 1]
            elif j == n - 1:
                matrix[i][j] = matrix[i + 1][j]
            elif i == n - 1:
                matrix[i][j] = matrix[i][j + 1]
    matrix[n - 1][n - 1] = 0
    return matrix


def hoca(n):
    if n == 1:
        return 1
    else:
        ans = 0
        res1 = hodga(n)
        res2 = horse(n)
        for i in range(len(res1)):
            for j in range(len(res1[i])):
                if res1[i][j] and res2[i][j]:
                    ans += res1[i][j] * res2[i][j]
                else:
                    ans += max(res1[i][j], res2[i][j])
    return ans


hoca_in = open('hoca.in', 'r')
hoca_out = open('hoca.out', 'w')

n = int(hoca_in.readline())
ans = hoca(n)
ans %= 9929
print(ans, file=hoca_out)
hoca_in.close()
hoca_out.close()
