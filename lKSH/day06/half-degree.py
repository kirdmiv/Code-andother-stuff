def half_degree(lst, n):
    res = [[0 for i in range(2)] for i in range(n)]
    for i in range(n):
        for j in range(len(lst[i])):
            if lst[i][j]:
                res[i][1] += 1
                res[j][0] += 1
    return res


half_degree_in = open('half-degree.in', 'r')
half_degree_out = open('half-degree.out', 'w')

n = int(half_degree_in.readline())
lst = [[]] * n
for i in range(n):
    lst[i] = list(map(int, half_degree_in.readline().split()))
ans = half_degree(lst, n)
for i in ans:
    print(' '.join([str(j) for j in i]), file=half_degree_out)
half_degree_in.close()
half_degree_out.close()
