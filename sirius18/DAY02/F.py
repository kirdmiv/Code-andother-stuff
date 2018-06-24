n, m = map(int, input().split())

if (n * m) % 4 != 0:
    print(-1)
else:
    ans = [[0] * m for i in range(n)]
    if n % 4 == 0:
        print(n * m // 4)
        cnt = 0
        res = 1
        for j in range(m):
            for i in range(n):
                ans[i][j] = res
                cnt += 1
                if cnt == 4:
                    res += 1
                    cnt = 0
    elif m % 4 == 0:
        print(n * m // 4)
        cnt = 0
        res = 1
        for i in range(n):
            for j in range(m):
                ans[i][j] = res
                cnt += 1
                if cnt == 4:
                    res += 1
                    cnt = 0
    else:
        print(n * m // 4)
        cnt = 0
        res = 1
        for i in range(0, n, 2):
            for j in range(m):
                ans[i][j] = res
                ans[i+1][j] = res
                cnt += 2
                if cnt == 4:
                    res += 1
                    cnt = 0
    for i in range(n):
        print(*ans[i])