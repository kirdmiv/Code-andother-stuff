def max_sort(lst):
    len_lst = len(lst)
    for i in range(len_lst - 1, -1, -1):
        max_index = i
        for j in range(i - 1, -1, -1):
            if lst[j] > lst[max_index]:
                max_index = j
        lst[max_index], lst[i] = lst[i], lst[max_index]
    return lst


n = int(input())
nums = list(map(int, input().split()))

res = max_sort(nums)
print(*res)
