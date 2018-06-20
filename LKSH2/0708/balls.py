import sys

sys.setrecursionlimit(10 ** 9)

SIZE = 11


def dfs(x, y, used):
    res = 0
    if 0 <= x < SIZE and 0 <= y < SIZE and graph[x][y] == current_letter and not used[x][y]:
        used[x][y] = True
        res = 1
        res += dfs(x - 1, y, used)
        res += dfs(x + 1, y, used)
        res += dfs(x, y - 1, used)
        res += dfs(x, y + 1, used)
    return res


balls_in = open('balls.in', 'r')
balls_out = open('balls.out', 'w')

graph = []
for i in range(SIZE):
    graph.append(list(balls_in.readline().rstrip()))
balls_in.close()

used = [[False] * SIZE for i in range(SIZE)]
letters = {'R': 0, 'B': 0, 'G': 0, 'Y': 0, 'V': 0}
ans_let = ['R', 'G', 'B', 'Y', 'V']

ans = []
for i in range(SIZE):
    for j in range(SIZE):
        current_letter = graph[i][j]
        res = dfs(i, j, used)
        res *= (res - 1)
        if res > 1 and letters[current_letter] < res:
            letters[current_letter] = res
for i in ans_let:
    print(i + ": " + str(letters[i]), file=balls_out)
balls_out.close()
