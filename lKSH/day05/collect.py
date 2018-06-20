def collect(lst, x):
    left, right = 0, len(lst)
    while left + 1 != right:
        middle = (left + right) // 2
        if lst[middle] <= x:
            left = middle
        else:
            right = middle
    if lst[left] == x:
        return 'YES'
    return 'NO'


collect_in = open('collect.in', 'r')
collect_out = open('collect.out', 'w')

num_of_butterflies = int(collect_in.readline())
butterflies_nums = list(map(int, collect_in.readline().split()))
num_of_new_butterflies = int(collect_in.readline())
new_butterflies_nums = list(map(int, collect_in.readline().split()))
collect_in.close()

ans = [0] * num_of_new_butterflies
for i in range(num_of_new_butterflies):
    ans[i] = collect(butterflies_nums, new_butterflies_nums[i])
print('\n'.join(ans), file=collect_out)
collect_out.close()
