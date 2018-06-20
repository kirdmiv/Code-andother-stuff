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


danger_in = open('danger.in', 'r')
danger_out = open('danger.out', 'w')

n, m = map(int, danger_in.readline().split())
start, finish = map(int, danger_in.readline().split())
start -= 1
finish -= 1

weigt = [[0] * n for i in range(n)]
for i in range(m):
    s, f, p = map(int, danger_in.readline().split())
    weigt[s - 1][f - 1] = 1 - (p / 100)
    weigt[f - 1][s - 1] = 1 - (p / 100)
danger_in.close()

print(1 - dijkstra(), file=danger_out)
danger_out.close()
