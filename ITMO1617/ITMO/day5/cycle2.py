def dfs(start):
    color[start] = 1
    for u in graph[start]:
        if color[u] == 0:
            cycleFound = dfs(u)
        elif color[start] == 1:
            cycleFound = True
    color[start] = 2
    return cycleFound


dfs_in = open('input.txt', 'r')
dfs_out = open('output.txt', 'w')

n = int(dfs_in.readline())
graph = []
for i in range(n):
    graph.append(list(map(int, dfs_in.readline().split())))
dfs_in.close()

color = [0] * (n + 1)
cycleFound = False

for i in range(n):
    if color[i] == 0:
        cycleFound = dfs(i)
        if cycleFound:
            print(1, file=dfs_out)
            exit()
print(0, file=dfs_out)
dfs_out.close()
