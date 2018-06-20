import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)


def mtoal(graph, n):
    res = [[] for i in range(n)]
    for i in range(n):
        for j in range(len(graph[i])):
            if graph[i][j]:
                res[i].append(j)
    return res


def bfs(graph, start, finish):
    queue = deque([start])
    dist = [None] * len(graph)
    dist[start] = 0
    while len(queue) != 0:
        v = queue.popleft()
        for i in graph[v]:
            if dist[i] is None:
                queue.append(i)
                dist[i] = dist[v] + 1
    return dist[finish]


bfs_in = open('bfs.in', 'r')
bfs_out = open('bfs.out', 'w')

n, s, f = map(int, bfs_in.readline().split())
graph = []
for i in range(n):
    graph.append(list(map(int, bfs_in.readline().split())))
bfs_in.close()

graph = mtoal(graph, n)
way_to_finish = bfs(graph, s - 1, f - 1)
if way_to_finish == None:
    print(0, file=bfs_out)
else:
    print(way_to_finish, file=bfs_out)
bfs_out.close()
