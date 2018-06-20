INF = 10 ** 9 + 7


def dijkstra():
    dist = [-INF] * n
    dist[start] = 1

    used = [False] * n

    max_dist = 1
    max_vertex = start

    while max_dist > -INF:
        i = max_vertex
        used[i] = True

        for j in range(n):
            if dist[i] * weigt[i][j] > dist[j]:
                dist[j] = dist[i] * weigt[i][j]

        max_dist = -INF
        for j in range(n):
            if not used[j] and dist[j] > max_dist:
                max_dist = dist[j]
                max_vertex = j
    return dist[finish]


fin = open("pathmgep.in", 'r')
fout = open("pathmgep.out", 'w')

n, st, fn = map(int, fin.readline().rstrip())
g = [[] for i in range(n)]
for i in range(n):
    a = list(map(int, fin.readline().split()))
    for j in range(n):
        if a[j] != -1:
            g[i].append((j, a[j]))
print(g)
fin.close()
fout.close()
