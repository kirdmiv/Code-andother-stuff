def merge(left, middle, right, storage):
    i, j = left, right
    for k in range(left, right):
        if i != middle and (j == right or lst[i] <= lst[j]):
            storage[k] = lst[i]
            i += 1
        else:
            storage[k] = lst[j]
            j += 1
    for k in range(left, right):
        lst[k] = storage[k]


def merge_sort(left, right, storage):
    if left == right - 1:
        return
    middle = (left + right) // 2
    merge_sort(left, middle, storage)
    merge_sort(middle, right, storage)
    merge(left, middle, right, storage)



lst = list(map(int, input().split()))
merge_sort(0, len(lst), storage)