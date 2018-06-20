import sys
import threading
threading.stack_size(2 * 67108864)
sys.setrecursionlimit(10 ** 9 + 7)


def main():
    # write your code here
    def dfs(x, y):
        ans = 0
        used[x][y] = True
        if graph[x][y] == '.':
            ans += 1
            if not used[x-1][y]:
                ans += dfs(x-1, y)
            if not used[x + 1][y]:
                ans += dfs(x + 1, y)
            if not used[x][y-1]:
                ans += dfs(x, y - 1)
            if not used[x][y + 1]:
                ans += dfs(x, y + 1)
        return ans

    fin = open("roomsquare.in", 'r')
    fout = open("roomsquare.out", 'w')

    n = int(fin.readline().rstrip())
    graph = [[] for i in range(n)]
    used = [[False] * n for i in range(n)]
    color = [0] * n
    ans = 0
    for i in range(n):
        graph[i] = list(fin.readline().rstrip())
    i, j = map(int, fin.readline().split())
    print(dfs(i-1, j-1), file=fout)
    fin.close()
    fout.close()
    pass


thread = threading.Thread(target=main)
thread.start()
