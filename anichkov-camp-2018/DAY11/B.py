import math

n, m = map(int, input().split())
a = [[]] * n
for i in range(n):
    a[i] = list(map(int, input().split()))

ans = 0
for i in range(int(math.ceil(n / 2))):
    for j in range(int(math.ceil(m / 2))):
        # print(i, j, ans)
        if (n % 2 == 1 and i == n - 2) or n == 1:
            if a[i][j] != a[i][-j - 1]:
                ans += 1
        elif (m % 2 == 1 and j == m - 2) or m == 1:
            if a[i][j] != a[-i - 1][j]:
                ans += 1
        else:
            k = [a[i][j], a[-i - 1][j], a[-i - 1][-j - 1], a[i][-j - 1]]
            k.sort()
            cnt = 1
            mc = 1
            for s in range(1, 4):
                if k[s] == k[s - 1]:
                    cnt += 1
                else:
                    mc = max(mc, cnt)
                    cnt = 1
            mc = max(mc, cnt)
            ans += 4 - mc
print(ans)
