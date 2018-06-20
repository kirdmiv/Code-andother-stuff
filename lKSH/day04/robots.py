import sys

sys.setrecursionlimit(10 ** 6)


def merge(lst, left, middle, right, storage):
    i, j = left, middle
    for k in range(left, right):
        if i != middle and (j == right or lst[i][0] <= lst[j][0]):
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


robots_in = open('robots.in', 'r')
robots_out = open('robots.out', 'w')

n = int(robots_in.readline())
lst = [] * n
for i in range(n):
    lst.append(list(map(int, robots_in.readline().split())))
robots_in.close()

if n == 1:
    print(' '.join([str(j) for j in lst[0]]), file=robots_out)
else:
    storage = [0] * len(lst)
    merge_sort(lst, 0, len(lst), storage)
    for i in storage:
        print(' '.join([str(j) for j in i]), file=robots_out)
robots_out.close()
