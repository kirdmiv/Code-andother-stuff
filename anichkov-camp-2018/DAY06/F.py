import sys
import threading
from collections import deque

threading.stack_size(2 * 67108864)
sys.setrecursionlimit(10 ** 9 + 7)


def main():
    # write your code here
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

    fin = open("pathbge1.in", 'r')
    fout = open("pathbge1.out", 'w')

    n, m = map(int, fin.readline().split())
    graph = [[] for i in range(n)]
    for i in range(m):
        a, b = map(int, fin.readline().split())
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)

    print(*bfs(0), file=fout)
    fin.close()
    fout.close()
    pass


thread = threading.Thread(target=main)
thread.start()
