def craft():
    num = 1
    while num < n:
        num *= 2
    num *= 2
    tree = [0] * num
    return tree


def update(tree, i, x):
    v = len(tree) // 2 + i
    tree[v] = x
    while v > 1:
        v //= 2
        tree[v] = tree[2 * v] + tree[2 * v + 1]
    return tree


def get_sum(v, begin, end, left, right):
    if (right <= begin) or (left >= end):
        return 0
    if left >= begin and right <= end:
        return tree[v]
    mid = (left + right) // 2
    return \
        get_sum(v * 2, begin, end, left, mid) + \
        get_sum(v * 2 + 1, begin, end, mid, right)


sumrooks_in = open('sum-rooks.in', 'r')
sumrooks_out = open('sum-rooks.out', 'w')

# Читаем
n, k = map(int, sumrooks_in.readline().split())
tree = craft()
for i in range(k):
    request, first, second = map(str, sumrooks_in.readline().split())
    first = int(first)
    second = int(second)
    if request == 'A':
        tree = update(tree, first - 1, second)
    else:
        print(get_sum(1, first - 1, second, 0, (len(tree) // 2)),
              file=sumrooks_out)
sumrooks_in.close()

sumrooks_out.close()
