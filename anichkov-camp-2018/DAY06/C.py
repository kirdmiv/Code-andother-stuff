import sys
import threading
threading.stack_size(67108864)
sys.setrecursionlimit(10 ** 9 + 7)


def main():
    # write your code here
    def dfs(u, c):
        color[u] = c
        for v in graph[u]:
            if color[v] == c:
                # print(u, v, color, c)
                return False
            if c == 1 and color[v] == 0:
                if not dfs(v, 2):
                    return False
            if c == 2 and color[v] == 0:
                if not dfs(v, 1):
                    return False
        return True

    fin = open("bipartite.in", 'r')
    fout = open("bipartite.out", 'w')

    n, m = map(int, fin.readline().split())
    graph = [[] for i in range(n)]
    color = [0] * n
    for i in range(m):
        a, b = map(int, fin.readline().split())
        a -= 1
        b -= 1
        if a == b:
            print("NO", file=fout)
            exit()
        if a not in graph[b]:
            graph[a].append(b)
            graph[b].append(a)

    for i in range(n):
        if color[i] == 0:
            if not dfs(i, 1):
                print("NO", file=fout)
                # print(graph, i, color)
                exit()
    print("YES", file=fout)
    fin.close()
    fout.close()
    pass


thread = threading.Thread(target=main)
thread.start()


