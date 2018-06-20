fin = open("bow.in", 'r')
fout = open("bow.out", 'w')

n = int(fin.readline())
x, d = map(int, fin.readline().split())
min_x = x - d
max_x = x + d
for i in range(n-1):
    x, d = map(int, fin.readline().split())
    cur_min = x - d
    cur_max = x + d
    if cur_max < min_x or cur_min > max_x:
        print(-1, file=fout)
        exit()
    else:
        min_x = max(min_x, cur_min)
        max_x = min(max_x, cur_max)

print(max_x, file=fout)
fin.close()
fout.close()