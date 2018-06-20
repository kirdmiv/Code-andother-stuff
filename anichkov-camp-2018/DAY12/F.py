h, w = map(int, input().split())
a = [input() for i in range(h)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
sides = "NWSE"
FAR = 10 ** 9
dist = [[FAR] * w for i in range(h)]
dist[0][0] = 0
changed = True
while changed:
    changed = False
    for i in range(h):
        for j in range(w):
            for d in range(4):
                ni = i + dx[d]
                nj = j + dy[d]
                if (0 <= ni < h) and (0 <= nj < w):
                    cost = 0 if a[i][j] == sides[d] else 1
                    if dist[ni][nj] > dist[i][j] + cost:
                        dist[ni][nj] = dist[i][j] + cost
                        changed = True
print(dist[-1][-1])
