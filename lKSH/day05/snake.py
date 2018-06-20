def snake(n):
    res = [[0] * n for i in range(n)]
    k = 0
    for i in range(n):
        for j in range(n):
            res[i][j] = j + (n * k) + 1
        k += 1
    for i in range(1, n, 2):
        res[i].sort(reverse=True)
    return res


snake_in = open('snake.in', 'r')
snake_out = open('snake.out', 'w')

n = int(snake_in.readline())
snake_in.close()

ans = snake(n)
for i in ans:
    print(' '.join([str(j) for j in i]), file=snake_out)
snake_out.close()
