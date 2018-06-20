n, a, b = map(int, input().split())
vals = list(map(int, input().split()))

dp = [[(False, 0)] * 201 for i in range(n+1)]
dp[0][100] = (True, -1)
ind = -1
for i in range(n):
    ind = -1
    for j in range(201):
        if dp[i][j][0] is True:
            if j + vals[i] - 100<= b:
                #print(j + vals[i] - 101)
                dp[i+1][j + vals[i]] = (True, 1)
                ind = j + vals[i]
            if j - vals[i] - 100 >= a:
                #print(j - vals[i] - 101)
                dp[i + 1][j - vals[i]] = (True, 0)
                ind = j - vals[i]

#6 0 8
#1 4 5 8 1 1
if ind == -1:
    print("Impossible")
    exit()

ans = []
for i in range(n):
    if dp[-i-1][ind][1] == 0:
        ans.append('0')
        ind += vals[-i-1]
    else:
        ans.append('1')
        ind -= vals[-i-1]

ans.reverse()
print(*ans, sep='')