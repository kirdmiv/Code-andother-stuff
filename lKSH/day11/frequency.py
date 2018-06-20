def frequency(d):
    res = list()
    for i in d:
        res.append((-d[i], i))
    res.sort()
    return res


frequency_in = open('frequency.in', 'r')
frequency_out = open('frequency.out', 'w')

d = dict()
i = 0
while i != '':
    i = frequency_in.readline().strip()
    tmp = i.split()
    for j in tmp:
        if not d.get(j, False):
            d[j] = 1
        else:
            d[j] += 1
frequency_in.close()

ans = frequency(d)
for i in ans:
    print(i[1], file=frequency_out)
frequency_out.close()
