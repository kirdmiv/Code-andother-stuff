company_in = open('company.in', 'r')
company_out = open('company.out', 'w')

lst = []
n = int(company_in.readline())
for i in range(n):
    k = int(company_in.readline())
    for j in range(k):
        res = list(company_in.readline().rstrip().split())
        time = list(map(int, res[0].split(':')))
        h = time[0] * 60
        m = time[1]
        s = time[2]
        time = ((h + m) * 60) + s
        lst.append([time, int(res[1])])
lst.sort()

b = 0
min_b = 0
for i in range(len(lst)):
    b += lst[i][1]
    if b < min_b:
        min_b = b
print(abs(min_b), file=company_out)
