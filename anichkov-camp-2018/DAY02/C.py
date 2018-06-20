inf = open("prizes.in", "r")

n, k = map(int, inf.readline().rstrip().split())
a = map(int, inf.readline().rstrip().split())
prefsum = [0]
s = 0
for x in a:
    s += x
    prefsum.append(s)

prefmax = [-1] * (n + 1)
for i in range(k, n + 1):
    L = prefsum[i] - prefsum[i - k]
    prefmax[i] = max(prefmax[i - 1], L)

suffmax = [-1] * (n + 1)
for i in range(n - k, -1, -1):
    L = prefsum[i + k] - prefsum[i]
    suffmax[i] = max(suffmax[i + 1], L)

ans = float("inf")
for i in range(0, n - k + 1):
    ans = min(ans, max(prefmax[i], suffmax[i + k]))

ouf = open("prizes.out", "w")
print(ans, file = ouf)

inf.close()
ouf.close()