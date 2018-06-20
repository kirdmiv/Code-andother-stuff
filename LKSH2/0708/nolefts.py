import sys

sys.setrecursionlimit(10 ** 9)


def dfs(x, y, used):
    res = 0
    if 0 <= x < n and 0 <= y < n and graph[x][y] == current_letter and not used[x][y]:
        used[x][y] = True
        res = 1
        res += dfs(x - 1, y, used)
        res += dfs(x + 1, y, used)
        res += dfs(x, y - 1, used)
        res += dfs(x, y + 1, used)
    return res


nolefts_in = open('nolefts.in', 'r')
nolefts_out = open('nolefts.out', 'w')

n, m = map(int, input().split())
graph = [[]] * n
for i in range(n):
    graph.append(list(nolefts_in.readline().rstrip()))
nolefts_in.close()

used = [[False] * n for i in range(n)]
letters = {'R': 0, 'B': 0, 'G': 0, 'Y': 0, 'V': 0}
ans_let = ['R', 'G', 'B', 'Y', 'V']

ans = []
for i in range(n):
    for j in range(n):
        current_letter = graph[i][j]
        res = dfs(i, j, used)
        res *= (res - 1)
        if res > 1 and letters[current_letter] < res:
            letters[current_letter] = res
for i in ans_let:
    print(i + ": " + str(letters[i]), file=nolefts_out)
nolefts_out.close()
