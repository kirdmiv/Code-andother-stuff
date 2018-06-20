def source(lst, n):
    res = [0]
    for i in range(n):
        tmp = 0
        for j in range(n):
            if not lst[j][i]:
                tmp += 1
        if tmp == n:
            res[0] += 1
            res.append(i + 1)
    return res


def sink(lst, n):
    res = [0]
    for i in range(n):
        tmp = 0
        for j in range(n):
            if not lst[i][j]:
                tmp += 1
        if tmp == n:
            res[0] += 1
            res.append(i + 1)
    return res


source_in = open('source.in', 'r')
source_out = open('source.out', 'w')

n = int(source_in.readline())
lst = [[]] * n
for i in range(n):
    lst[i] = list(map(int, source_in.readline().split()))
source_in.close()

source = source(lst, n)
sink = sink(lst, n)
print(' '.join([str(i) for i in source]), file=source_out)
print(' '.join([str(i) for i in sink]), file=source_out)
source_out.close()
