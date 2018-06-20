from collections import deque


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
    prev = [None] * len(graph)
    dist[start] = 0
    while len(queue) != 0:
        v = queue.popleft()
        for i in graph[v]:
            if dist[i] is None:
                queue.append(i)
                dist[i] = dist[v] + 1
                prev[i] = v
    if dist[finish] is None:
        return -1, 0
    way = [str(finish + 1)]
    current = finish
    for i in range(dist[finish]):
        current = prev[current]
        way.append(str(current + 1))
    way.reverse()
    return dist[finish], way


path_in = open('path.in', 'r')
path_out = open('path.out', 'w')

n = int(path_in.readline())
graph = []
for i in range(n):
    graph.append(list(map(int, path_in.readline().split())))
s, f = map(int, path_in.readline().split())
path_in.close()

graph = mtoal(graph, n)
res, way_to_finish = bfs(graph, s - 1, f - 1)
print(res, file=path_out)
if res != -1:
    print(' '.join(way_to_finish), file=path_out)
path_out.close()
