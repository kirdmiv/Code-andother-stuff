def muggers(lst, n, k):
    stair = [0] * n
    for i in range(k + 1, n):
        j = i - k - 1
        lst[i] += min(lst[j:i])
    return lst[n - 1]


muggers_in = open('muggers.in', 'r')
muggers_out = open('muggers.out', 'w')

n, k = map(int, muggers_in.readline().split())
lst = list(map(int, muggers_in.readline().split()))
print(muggers(lst, n, k), file=muggers_out)
muggers_in.close()
muggers_out.close()
