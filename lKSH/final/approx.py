def bin_s(lst, num):
    left, right = -1, len(lst)
    while left + 1 != right:
        middle = (left + right) // 2
        if lst[middle] < num:
            left = middle
        else:
            right = middle
    if abs(lst[right] - num) < abs(lst[left] - num):
        return lst[right]
    if left == -1:
        return lst[0]
    return lst[left]


def approx(first_lst, second_lst):
    ans = []
    for i in second_lst:
        ans.append(bin_s(first_lst, i))
    return ans


approx_in = open('approx.in', 'r')
approx_out = open('approx.out', 'w')

n, m = approx_in.readline().split()
first_lst = list(map(int, approx_in.readline().split()))
second_lst = list(map(int, approx_in.readline().split()))
approx_in.close()

ans = approx(first_lst, second_lst)
for i in ans:
    print(i, file=approx_out)
approx_out.close()
