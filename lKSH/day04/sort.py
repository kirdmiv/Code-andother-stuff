import sys
sys.setrecursionlimit(10 ** 6)


def merge(lst, left, middle, right, storage):
    i, j = left, middle
    for k in range(left, right):
        if i != middle and (j == right or lst[i] <= lst[j]):
            storage[k] = lst[i]
            i += 1
        else:
            storage[k] = lst[j]
            j += 1
    for k in range(left, right):
        lst[k] = storage[k]


def merge_sort(lst, left, right, storage):
    if right == left + 1:
        return
    middle = (right + left) // 2
    merge_sort(lst, left, middle, storage)
    merge_sort(lst, middle, right, storage)
    merge(lst, left, middle, right, storage)


sort_in = open('sort.in', 'r')
sort_out = open('sort.out', 'w')

n = sort_in.readline()
lst = list(map(int, sort_in.readline().split()))
sort_in.close()

storage = [0] * len(lst)
merge_sort(lst, 0, len(lst), storage)
ans = [str(i) for i in lst]
ans = ' '.join(ans)
sort_out.write(ans)
sort_out.close()
