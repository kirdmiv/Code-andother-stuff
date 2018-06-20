import sys

sys.setrecursionlimit(10 ** 6)


def labirint(graph, r, c, used):
    res = 0
    if used[r][c]:
        return 0
    used[r][c] = True
    if graph[r][c] == '*':
        return 0
    if graph[r][c] == '.':
        res += 1
    res += labirint(graph, r + 1, c, used)
    res += labirint(graph, r - 1, c, used)
    res += labirint(graph, r, c + 1, used)
    res += labirint(graph, r, c - 1, used)
    return res


file_in = open('input.txt', 'r')
file_out = open('output.txt', 'w')

n = int(file_in.readline())
graph = []
for i in range(n):
    graph.append(list(file_in.readline().strip()))
r, c = map(int, file_in.readline().split())
file_in.close()

used = [[False] * n for i in range(n)]
print(labirint(graph, r - 1, c - 1, used), file=file_out)
file_out.close()
