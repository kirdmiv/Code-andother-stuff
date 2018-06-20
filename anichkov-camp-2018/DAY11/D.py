n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

pref_a = [0] * n
pref_a[0] = a[0]
for i in range(1, n):
    pref_a[i] = pref_a[i-1] + a[i]

pref_b = [0] * m
pref_b[0] = b[0]
for i in range(1, m):
    pref_b[i] = pref_b[i-1] + b[i]

ans = 0
for cur in range(1, n):
    max_l = min(n-cur, m+cur)-1
    ans += cur * abs(pref_a[max_l+cur] - pref_a[cur-1] - pref_b[max_l])
    print(ans, max_l)

print(ans)

for cur in range(1, m):
    max_l = min(n+cur, m-cur)-1
    ans += -cur * abs(pref_a[max_l] - pref_b[max_l+cur] + pref_b[cur-1])

print(ans)