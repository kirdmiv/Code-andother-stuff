import sys
import threading
threading.stack_size(2 * 67108864)
sys.setrecursionlimit(10 ** 9 + 7)


def main():
    # write your code here
    def dfs(u):
        color[u] = 1
        for v in graph[u]:
            if color[v] == 0:
                ans.append((u+1, v+1))
                dfs(v)
        return

    fin = open("graph2tree.in", 'r')
    fout = open("graph2tree.out", 'w')

    n, m = map(int, fin.readline().split())
    graph = [[] for i in range(n)]
    color = [0] * n
    ans = []
    for i in range(m):
        a, b = map(int, fin.readline().split())
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)
    dfs(0)
    for slon in ans:
        print(*slon, file=fout)
    fin.close()
    fout.close()
    pass


thread = threading.Thread(target=main)
thread.start()
