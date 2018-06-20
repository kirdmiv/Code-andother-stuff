import sys
import threading
threading.stack_size(2 * 67108864)
sys.setrecursionlimit(10 ** 9 + 7)

def main():
    def printAns(beg, end):
        path = []
        while beg != end:
            path.append(beg + 1)
            beg = prev[beg]
        path.append(end + 1)
        path.reverse()
        print("YES")
        print(len(path))
        print(*path)
        exit()

    def dfs(u, pred):
        color[u] = 1
        prev[u] = pred
        for v in graph[u]:
            if color[v] == 1:
                # print(u, v, color, c)
                printAns(v, u)
                return True
            if color[v] == 0:
                # print(u, v, color, c)
                dfs(v, u)
        color[u] = 2
        return

    #fin = open("cycle.in", 'r')
    #fout = open("cycle.out", 'w')

    #n, m = map(int, fin.readline().split())
    n, m = map(int, input().split())
    graph = [[] for i in range(n)]
    color = [0] * n
    prev = [0] * n
    for i in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        graph[a].append(b)

    for i in range(n):
        if color[i] == 0:
            dfs(i, -1)
    print("NO")
    pass


thread = threading.Thread(target=main)
thread.start()