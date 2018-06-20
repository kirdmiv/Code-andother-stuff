INF = 10 ** 9 + 7

import sys
import threading
from collections import deque
threading.stack_size(2 * 67108864)
sys.setrecursionlimit(INF)


def main():
    # write your code here

    def bfs(start):
        queue = deque([start])
        dist = [None] * n
        dist[start] = 0
        while len(queue) != 0:
            v = queue.popleft()
            for i in graph[v]:
                if dist[i] is None and kakoyto_massiv[i] - kakoyto_massiv[v] == 0:
                    queue.appendleft(i)
                    dist[i] = dist[v]
                    prev[i] = v
                elif dist[i] is None:
                    queue.append(i)
                    dist[i] = dist[v] + 1
                    prev[i] = v
        return dist

    fin = open("island.in", 'r')
    fout = open("island.out", 'w')

    n, m = map(int, fin.readline().split())
    graph = [[] for i in range(n)]
    kakoyto_massiv = list(map(int, fin.readline().split()))
    dp = [INF] * n
    prev = [0] * n
    for i in range(m):
        a, b = map(int, fin.readline().split())
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)
    dp[0] = 0
    dist = bfs(0)
    if dist[-1] is None:
        print("impossible", file=fout)
    else:
        beg = n-1
        end = 0
        path = []
        while beg != end:
            path.append(beg + 1)
            beg = prev[beg]
        path.append(end + 1)
        path.reverse()
        print(dist[-1], len(path), file=fout)
        print(*path, file=fout)
        exit()
    fin.close()
    fout.close()
    pass


thread = threading.Thread(target=main)
thread.start()
