def cnt_sort(a):
    maxval = 200000
    cnt = [0] * maxval
    for i in a:
        cnt[i] += 1
    res = []
    for i in range(maxval):
        res += [i] * cnt[i]
    return res


count_sort_in = open('countsort.in', 'r')
count_sort_out = open('countsort.out', 'w')

n = count_sort_in.readline()
lst = list(map(int, count_sort_in.readline().split()))
count_sort_in.close()

res = cnt_sort(lst)
ans = [str(i) for i in res]
ans = ' '.join(ans)
count_sort_out.write(ans)
count_sort_out.close()
