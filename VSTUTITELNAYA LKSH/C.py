from collections import deque


def bfs(start):
    queue = deque([start])
    dist = [None] * n
    dist[start] = 0
    while len(queue) != 0:
        v = queue.popleft()
        for i in graph[v]:
            if dist[i] is None:
                queue.append(i)
                dist[i] = dist[v] + 1
    return dist


n, m, t = map(int, input().split())
a = list(map(int, input().split()))
graph = [[] for i in range(n)]
for i in range(m):
    b, e = map(int, input().split())
    b -= 1
    e -= 1
    graph[b].append(e)
    graph[e].append(b)
s, w = map(int, input().split())
s -= 1
d1 = bfs(s)
d = []
for i in range(len(d1)):
    if d1[i] is not None:
        d.append((d1[i], i))
d.sort()

cur = 0
minuta = 0
pointer = 0
f = False
while w > 0:
    while pointer < len(d) and d[pointer][0] == minuta:
        cur += a[d[pointer][1]]
        pointer += 1
    k = min(cur, w, t)
    cur -= k
    w -= k
    if cur == 0 and w > 0:
        f = True
        break
    minuta += 1

if f:
    print("YES")
else:
    print("NO")
