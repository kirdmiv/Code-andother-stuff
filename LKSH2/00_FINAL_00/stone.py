import sys

sys.setrecursionlimit(10 ** 9)

SIZE = 11


def dfs(x, y, used):
    if x == position[0] and y == position[1]:
        return True
    if 0 <= x < SIZE and 0 <= y < SIZE and not used[x][y] and field[x][y]:
        used[x][y] = True
        if dfs(x - 1, y, used):
            return True
        if dfs(x + 1, y, used):
            return True
        if dfs(x, y - 1, used):
            return True
        if dfs(x, y + 1, used):
            return True

        if dfs(x - 1, y - 1, used):
            return True
        if dfs(x + 1, y + 1, used):
            return True
        if dfs(x + 1, y - 1, used):
            return True
        if dfs(x - 1, y + 1, used):
            return True
    return False


field = [[True] * SIZE for i in range(SIZE)]

stone_in = open('stone.in', 'r')
stone_out = open('stone.out', 'w')

harry = list(map(str, stone_in.readline().rstrip()))
harry[0] = ord(harry[0]) - ord('a')
harry[1] = int(harry[1]) - 1

position = list(map(str, stone_in.readline().rstrip()))
position[0] = ord(position[0]) - ord('a')
position[1] = int(position[1]) - 1

telepusya = int(stone_in.readline())

for i in range(telepusya):
    pos = list(map(str, stone_in.readline().rstrip()))
    pos[0] = ord(pos[0]) - ord('a')
    pos[1] = int(pos[1]) - 1
    field[pos[0]][pos[1]] = False

konya = int(stone_in.readline())

for i in range(konya):
    pos = list(map(str, stone_in.readline().rstrip()))
    pos[0] = ord(pos[0]) - ord('a')
    pos[1] = int(pos[1]) - 1
    field[pos[0]][pos[1]] = False
    k = pos[0] - 2
    j = pos[1] - 1
    if 0 <= k < SIZE and 0 <= j < SIZE:
        field[k][j] = False
    k = pos[0] - 1
    j = pos[1] - 2
    if 0 <= k < SIZE and 0 <= j < SIZE:
        field[k][j] = False
    k = pos[0] - 2
    j = pos[1] + 1
    if 0 <= k < SIZE and 0 <= j < SIZE:
        field[k][j] = False
    k = pos[0] - 1
    j = pos[1] + 2
    if 0 <= k < SIZE and 0 <= j < SIZE:
        field[k][j] = False
    k = pos[0] + 2
    j = pos[1] - 1
    if 0 <= k < SIZE and 0 <= j < SIZE:
        field[k][j] = False
    k = pos[0] + 2
    j = pos[1] + 1
    if 0 <= k < SIZE and 0 <= j < SIZE:
        field[k][j] = False
    k = pos[0] + 1
    j = pos[1] + 2
    if 0 <= k < SIZE and 0 <= j < SIZE:
        field[k][j] = False
    k = pos[0] + 1
    j = pos[1] - 2
    if 0 <= k < SIZE and 0 <= j < SIZE:
        field[k][j] = False

used = [[False] * SIZE for i in range(SIZE)]
ans = []
res = dfs(harry[0], harry[1], used)
if res:
    print("YES", file=stone_out)
else:
    print("NO", file=stone_out)
stone_out.close()
