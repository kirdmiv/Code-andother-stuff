from collections import deque


def from_edge(n, lst):
    new_lst = [[] for i in range(n)]
    for i in lst:
        j = i[0] - 1
        k = i[1] - 1
        new_lst[k].append(i[0] - 1)
        new_lst[j].append(i[1] - 1)
    return new_lst


def bfs(graph, n):
    for start in range(n - 1):
        for finish in range(start, n):
            queue = deque([start])
            dist = [None] * len(graph)
            dist[start] = 0
            while len(queue) != 0:
                v = queue.popleft()
                for i in graph[v]:
                    if dist[i] is None:
                        queue.append(i)
                        dist[i] = dist[v] + 1
            dist_finish = dist[finish]
            if (dist_finish is None) or dist_finish > 2:
                return 'NO'
    return 'YES'


two_in = open('two.in', 'r')
two_out = open('two.out', 'w')

n, m = map(int, two_in.readline().split())
graph = []
for i in range(m):
    graph.append(list(map(int, two_in.readline().split())))
two_in.close()

graph = from_edge(n, graph)
print(bfs(graph, n), file=two_out)
two_out.close()
