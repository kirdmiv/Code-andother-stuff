fin = open("friends.in", 'r')
fout = open("friends.out", 'w')

n, m = map(int, fin.readline().split())
a = list(map(int, fin.readline().split()))
b = list(map(int, fin.readline().split()))

for i in range(n):
    a[i] = [a[i], i]

for j in range(m):
    b[j] = [b[j], j]

a.sort(reverse=True)
b.sort(reverse=True)

ans = []
a.sort(reverse=True)
b.sort(reverse=True)

#print(a, b)
for i in range(n):
    b.sort(reverse=True)
    for j in range(m):
        if a[i][0] > 0 and b[j][0] > 0:
            # print(i, j, a, b)
            a[i][0] -= 1
            b[j][0] -= 1
            ans.append((a[i][1] + 1, b[j][1] + 1))
#print(a, b)
s1 = 0
for i in range(n):
    s1 += a[i][0]
s2 = 0
for i in range(m):
    s2 += b[i][0]
#print(s1, s2)
if s1 > 0 or s2 > 0:
    print("NO", file=fout)
else:
    print("YES", file=fout)
    print(len(ans), file=fout)
    for i in ans:
        print(*i, file=fout)

fin.close()
fout.close()
