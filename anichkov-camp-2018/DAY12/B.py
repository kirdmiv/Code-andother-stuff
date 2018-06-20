n, p = map(int, input().split())
a = list(map(int, input().split()))

pref_sum = [0] * n
pref_sum[0] = a[0]
for i in range(1, n):
    pref_sum[i] = pref_sum[i - 1] + a[i]

for i in range(n):
    for j in range(n):
        #print(i, j)
        if j + i < n:
            res = pref_sum[i + j]
            if j > 0:
                res -= pref_sum[j - 1]
        else:
            res = pref_sum[-1] + pref_sum[i - n + j]
            #print(j + 1, i + 1, pref_sum)
            if j > 0:
                res -= pref_sum[j - 1]
        if res >= p:
            print(j + 1, i + 1)
            exit()

print(-1)
