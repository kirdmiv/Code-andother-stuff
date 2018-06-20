fin = open("droids.in", 'r')
fout = open("droids.out", 'w')

n, m = map(int, fin.readline().split())
line = list(fin.readline().rstrip())
alg = fin.readline().rstrip()
max_l = 0
max_r = 0
cur_l = 0
cur_r = 0
for i in range(m):
    if alg[i] == 'L':
        cur_l += 1
        cur_r -= 1
    else:
        cur_l -= 1
        cur_r += 1
    max_l = max(max_l, cur_l)
    max_r = max(max_r, cur_r)

block = n
for i in range(n-1, -1, -1):
    if line[i] == '#':
        block = i
    elif line[i] == 'D':
        if block - i <= max_r:
            line[i] = '.'


ans = []
block = -1
for i in range(n):
    if line[i] == '#':
        block = i
    elif line[i] == 'D':
        if i - block > max_l:
            ans.append(i+1)

print(len(ans), file=fout)
print(*ans, file=fout)


fin.close()
fout.close()
