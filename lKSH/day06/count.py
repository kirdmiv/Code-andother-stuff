def count(lst):
    res = 0
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j]:
                res += 1
    return res // 2


count_in = open('count.in', 'r')
count_out = open('count.out', 'w')

n = int(count_in.readline())
lst = [[]] * n
for i in range(n):
    lst[i] = list(map(int, count_in.readline().split()))
print(count(lst), file=count_out)
count_in.close()
count_out.close()
