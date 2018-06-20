INF = 10 ** 9 + 7


def bellman():
    for k in range(1, nights + 1):
        for i in range(n):
            for j in range(n):
                dp[j][k] = min(dp[j][k], dp[i][k - 1] + graph[i][j])

                min_ans = min(dp[finish])
    if min_ans == INF:
        return -1
    return min_ans


avia_in = open('avia2.in', 'r')
avia_out = open('avia2.out', 'w')

n, m, nights, start, finish = map(int, avia_in.readline().split())
start -= 1
finish -= 1
dp = [[INF] * (nights + 1) for i in range(n + 1)]
dp[start][0] = 0

graph = [[INF] * n for i in range(n + 1)]

for i in range(m):
    s, f, p = map(int, avia_in.readline().split())
    graph[s - 1][f - 1] = min(graph[s - 1][f - 1], p)
avia_in.close()

print(bellman(), file=avia_out)
avia_out.close()
