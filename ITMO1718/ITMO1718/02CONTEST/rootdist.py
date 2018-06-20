fin = open("rootdist.in", 'r')
fout = open("rootdist.out", 'w')

n = int(fin.readline())
lst = [0 for i in range(n)]
for i in range(n - 1):
    lst[i + 1] = int(fin.readline())

fans = max(lst)
print(fans, file=fout)
res = 0
ans = []
for i in range(n):
    if lst[i] == fans:
        res += 1
        ans.append(i + 1)
print(res, file=fout)
print(*ans, file=fout)