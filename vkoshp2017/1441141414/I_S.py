fin = open("sochi.in", "r")
fout = open("sochi.out", "w")

n, d = map(int, fin.readline().split())
a = list(map(int, fin.readline().split()))
a.sort(reverse=True)
ans = a[0]
left = 0
right = 0
cur = True
for i in range(1, n):
    if cur:
        if a[i] > 2 * d and a[right] >= 2 * d:
            ans += a[i] - d - d
            a[right] -= d
            a[i] -= d
            right = i
    else:
        if a[i] > 2 * d and a[left] >= 2 * d:
            ans += a[i] - d - d
            a[left] -= d
            a[i] -= d
            left = i
    cur = not cur

print(ans, file=fout)



fin.close()
fout.close()