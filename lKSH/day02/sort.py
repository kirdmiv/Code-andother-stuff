def min_sort(lst):
    len_lst = len(lst)
    for i in range(len_lst):
        min_index = i
        for j in range(i, len_lst):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[min_index], lst[i] = lst[i], lst[min_index]
    return lst


sortin = open('sort.in', 'r')
sortout = open('sort.out', 'w')

n = sortin.readline()
nums = list(map(int, sortin.readline().split()))
sortin.close()

res = min_sort(nums)
ans = [str(i) for i in res]
ans = ' '.join(ans)
sortout.write(ans)
sortout.close()
