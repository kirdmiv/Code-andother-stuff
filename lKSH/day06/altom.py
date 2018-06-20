def altom(lst, n):
    res = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(1, lst[i][0] + 1):
            num = lst[i][j]
            res[i][num - 1] = 1
    return res


altom_in = open('altom.in', 'r')
altom_out = open('altom.out', 'w')

n = int(altom_in.readline())
lst = []
for i in range(n):
    lst.append(list(map(int, altom_in.readline().split())))
altom_in.close()

ans = altom(lst, n)
for i in ans:
    print(' '.join([str(j) for j in i]), file=altom_out)
altom_out.close()
