def check(lst, n, m):
    ans = [[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        num1 = lst[i][0]
        num2 = lst[i][1]
        res = ans[num1 - 1][num2 - 1]
        if res == 1:
            return 'YES'
        ans[num1 - 1][num2 - 1] = 1
    return 'NO'


check_in = open('check.in', 'r')
check_out = open('check.out', 'w')

n, m = map(int, check_in.readline().split())
lst = []
for i in range(m):
    lst.append(list(map(int, check_in.readline().split())))
check_in.close()

print(check(lst, n, m), file=check_out)
check_out.close()
