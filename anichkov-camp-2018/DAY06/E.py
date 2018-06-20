import sys
import threading
threading.stack_size(2 * 67108864)
sys.setrecursionlimit(10 ** 9 + 7)


def main():
    # write your code here
    def dfs(u, fout):
        color[u] = 1
        for v in graph[u]:
            if color[v] == 1:
                print(-1, file=fout)
                exit()
            if color[v] == 0:
                dfs(v, fout)
        ans.append(u+1)
        color[u] = 2
        return

    fin = open("topsort.in", 'r')
    fout = open("topsort.out", 'w')

    n, m = map(int, fin.readline().split())
    graph = [[] for i in range(n)]
    color = [0] * n
    ans = []
    for i in range(m):
        a, b = map(int, fin.readline().split())
        a -= 1
        b -= 1
        graph[a].append(b)

    for i in range(n):
        if color[i] == 0:
            dfs(i, fout)
    print(*reversed(ans), file=fout)
    fin.close()
    fout.close()
    pass


thread = threading.Thread(target=main)
thread.start()
