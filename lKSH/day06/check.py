def check(lst, colors):
    res = 'YES'
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if i == j and lst[i][j] == 1:
                res = 'NO'
            elif lst[i][j] != lst[j][i]:
                res = 'NO'
    return res


check_in = open('check.in', 'r')
check_out = open('check.out', 'w')

n = int(check_in.readline())
lst = []
for i in range(n):
    lst.append(list(map(int, check_in.readline().split())))
colors = list(map(int, check_in.readline().split()))
print(check(lst, colors), file=check_out)
check_in.close()
check_out.close()
