def get_cop(t, x, y):
    return t // x + t // y


def bin_search(num, x, y):
    left, right = 0, num * x + 1
    while left + 1 != right:
        middle = (left + right) // 2
        if get_cop(middle, x, y) < num:
            left = middle
        else:
            right = middle
    return right


def easy(n, x, y):
    res = min(x, y)
    if n != 1:
        res += bin_search(n - 1, x, y)
    return res


easy_in = open('easy.in', 'r')
easy_out = open('easy.out', 'w')

n, x, y = map(int, easy_in.readline().split())
easy_in.close()

print(easy(n, x, y), file=easy_out)
easy_in.close()