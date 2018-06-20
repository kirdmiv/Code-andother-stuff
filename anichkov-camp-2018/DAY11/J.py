n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)
mint = a[-1]
maxt = mint
ans = 0
for i in range(n-1):
    if a[i] == mint:
        break
    t1 = a[i]/2
    maxt = max(maxt, t1)
    mint = min(mint, t1)
    ans = max(ans, mint/max(maxt, a[i+1]))
    #print(t1, ans, a, i, maxt, mint)
ans = max(ans, mint/max(maxt, a[i+1]))
print(ans)