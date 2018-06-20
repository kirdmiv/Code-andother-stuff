def smt(x, y):
    for i in range(n):
        steps[i] = numberOfSteps(x + dx[i], y + dy[i], board)
    for i in range(n):
        if steps[i] > 0:
            idx = i
            break
    if i == n - 1:
        for i in range(n):
            if steps[i] == 0:
                board[x + dx[i]][y + dy[i]] = count
        print(board)
        return 0
    for i in range(n):
        if steps[i] < steps[idx] and steps[i] > 0:
            idx = i
    x += dx[idx]
    y += dy[idx]
    board[x][y] = count
    return 0


def numberOfSteps(x, y, board):
    if x < 0 or x >= n or y < 0 or y >= m or board[x][y] != 0:
        return -1
    count = 0
    for k in range(n):
        xn = x + dx[k]
        yn = y + dy[k]
    if xn >= 0 and xn < n and yn >= 0 and yn < m and board[xn][yn] == 0:
        count += 1
    return count


def gen(board, x, y, k):
    ans.append([x, y])
    if k == 0:
        print(ans)
        return True
    for i in range(len(board)):
        newx = x + dx[i]
        newy = y + dy[i]
        if not board[newx][newy]:
            board[newx][newy] = 1
    if gen(board, newx, newy, k - 1):
        board[newx][newy] = 0
        return True
    ans.pop()
    return False


count = 1
idx = 0
ans = []
n, m = map(int, input().split())
board = [[0] * n for i in range(m)]
board[1][1] = count
steps = [0] * n * m
dx = [-1, -1, 1, 1, 2, 2, -2, -2]
dy = [2, -2, 2, -2, 1, -1, 1, -1]
smt(0, 0)
print(board)
print(steps)
