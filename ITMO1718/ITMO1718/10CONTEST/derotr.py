def build(lst, v, left, right):
    print(left, lst, v)
    if left == right:
        tree[v] = lst[left]
    else:
        mid = (left + right) // 2
        build(lst, v * 2, left, mid)
        build(lst, v * 2 + 1, mid + 1, right)
        tree[v] = max(tree[v * 2], tree[v * 2 + 1])


def update(v, left, right, i, x):
    if left == right:
        tree[v] = x
    else:
        mid = (left + right) // 2
        if i <= mid:
            update(v * 2, left, mid, i, x)
        else:
            update(v * 2 + 1, mid + 1, right, i, x)
    print(tree, lst)
    tree[v] = max(tree[v * 2], tree[v * 2 + 1])


def get_max(v, begin, end, left, right):
    if (right <= begin) or (left >= end):
        return 0
    if left >= begin and right <= end:
        return tree[v]
    mid = (left + right) // 2
    return \
        max(get_max(v * 2, begin, end, left, mid),
            get_max(v * 2 + 1, begin, end, mid, right))


rqt_in = open('rmq.in', 'r')
rqt_out = open('rmq.out', 'w')

n, q = map(int, rqt_in.readline().split())
tree = [0] * n * 2
lst = list(map(int, rqt_in.readline().split()))
build(lst, 1, 0, n)
for i in range(q):
    req = list(map(str, rqt_in.readline().split()))
    if req[0] == 'add':
        update(1, int(req[1]) - 1, int(req[2]), 0, int(req[3]))
    else:
        print(get_max(1, int(req[1]) - 1, int(req[2]), 0, (len(tree) // 2)),
              file=rqt_out)
rqt_in.close()

rqt_out.close()
