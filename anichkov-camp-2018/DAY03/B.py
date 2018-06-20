fin = open("input.txt", 'r')
fout = open("output.txt", 'w')

n, m, d, k = map(int, fin.readline().split())
lst = [0] * m
for i in range(k):
    x, y, z = map(int, fin.readline().split())
    lst[y - 1] += z

prefsum = [0] * (m + 1)
for i in range(m):
    prefsum[i + 1] = prefsum[i] + lst[i]

minpref = [0] * m
minpref[0] = prefsum[0]
for i in range(1, m):
    minpref[i] = min(minpref[i - 1], lst[i])

maxp = prefsum[d - 1]
ind = 1
# print(maxp)
#print(lst, prefsum)
for i in range(d - 1, m):
#    print(i, prefsum[i + 1] - prefsum[i - d + 1], prefsum[i + 1] - prefsum[i - d + 1] > maxp, maxp)
    if (prefsum[i + 1] - prefsum[i - d + 1]) > maxp:
#        print(maxp, "wut")
        maxp = prefsum[i + 1] - prefsum[i - d + 1]
        ind = i - d + 2
#        print(ind)
print(ind, file=fout)

fin.close()
fout.close()