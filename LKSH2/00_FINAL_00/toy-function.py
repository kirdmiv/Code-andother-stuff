def main():
    def craft():
        tree = [0] * (2 ** 18)
        return tree

    def update(tree, i, x):
        v = len(tree) // 2 + i
        tree[v] += x
        while v > 1:
            v //= 2
            tree[v] = evklidich(tree[2 * v], tree[2 * v + 1])
        return tree

    def evklidich(a, b):
        a = abs(a)
        b = abs(b)
        while a > 0 and b > 0:
            if a > b:
                a %= b
            else:
                b %= a
        return max(a, b)

    def get_sum(v, begin, end, left, right):
        if (right <= begin) or (left >= end):
            return 0
        if left >= begin and right <= end:
            return tree[v]
        mid = (left + right) // 2
        return \
            evklidich(get_sum(v * 2, begin, end, left, mid),
                      get_sum(v * 2 + 1, begin, end, mid, right))

    toy_function_in = open('toy-function.in', 'r')
    toy_function_out = open('toy-function.out', 'w')

    # Читаем
    n = int(toy_function_in.readline())
    tree = craft()
    for i in range(n):
        request, first, second = map(str, toy_function_in.readline().split())
        first = int(first)
        second = int(second)
        if request == '1':
            tree = update(tree, first - 1, second)
        else:
            print(get_sum(1, first - 1, second, 0, (len(tree) // 2)),
                  file=toy_function_out)

    toy_function_in.close()
    toy_function_out.close()
    return


main()
