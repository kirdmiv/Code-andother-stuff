import sys
sys.setrecursionlimit(int(1e9))

MAXN = 300
s = ["SOUTH", "WEST", "NORTH", "EAST"]
y = [1, 0, -1, 0]
x = [0, -1, 0, 1]

def dfs(i, j):
    a[i][j] = 1
    for k in range(4):
        if not a[i+y[k]][j+x[k]]:
            print(s[k])
            r = input()
            if r != "BLOCKED":
                dfs(i+y[k], j+x[k])


a = [[0] * MAXN for i in range(MAXN)]

dfs(150, 150)
print("DONE")