def mtoal(lst, n):
    res = [[0] for i in range(n)]
    for i in range(n):
        for j in range(len(lst[i])):
            if lst[i][j]:
                res[i][0] += 1
                res[i].append(j + 1)
    return res


mtoal_in = open('mtoal.in', 'r')
mtoal_out = open('mtoal.out', 'w')

n = int(mtoal_in.readline())
lst = [[]] * n
for i in range(n):
    lst[i] = list(map(int, mtoal_in.readline().split()))
ans = mtoal(lst, n)
for i in ans:
    print(' '.join([str(j) for j in i]), file=mtoal_out)
mtoal_in.close()
mtoal_out.close()
