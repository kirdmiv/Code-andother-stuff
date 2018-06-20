import sys
from collections import deque

sys.setrecursionlimit(10 ** 9)

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

numbers_in = open('numbers.in', 'r')
numbers_out = open('numbers.out', 'w')

graph = []
for i in range(SIZE):
    graph.append(list(numbers_in.readline().rstrip()))
numbers_in.close()

print(i + ": " + str(letters[i]), file=numbers_out)
numbers_out.close()