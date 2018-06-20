import heapq
fin = open("calc.in", 'r')
fout = open("calc.out", 'w')

n = int(fin.readline().rstrip())
a = list(map(int, fin.readline().split()))
heapq.heapify(a)
res = 0
for i in range(1, n):
    m1 = heapq.heappop(a)
    m2 = heapq.heappop(a)
    s = m1 + m2
    res += 0.05 * s
    heapq.heappush(a, s)
res = "{:.2f}".format(res)
print(res, file=fout)
fin.close()
fout.close()
