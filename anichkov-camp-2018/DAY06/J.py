INF = 10 ** 9 + 7
from collections import deque


def bfs(start):
    queue = deque([start])
    dist = [None] * n
    dist[start] = 0
    while len(queue) != 0:
        v = queue.popleft()
        i1 = v + 1
        i2 = v * 2
        if i1 >= n:
            i1 -= n
        if i2 >= n:
            i2 -= n
        if dist[i1] is None:
            queue.append(i1)
            dist[i1] = dist[v] + 1
        if dist[i2] is None:
            queue.append(i2)
            dist[i2] = dist[v] + 1
    return dist


fin = open("numbers.in", 'r')
fout = open("numbers.out", 'w')

n, m, to_chto_nuzn = map(int, fin.readline().split())
if m == n:
    m = 0
if to_chto_nuzn == n:
    to_chto_nuzn = 0

print(bfs(m)[to_chto_nuzn], file=fout)
