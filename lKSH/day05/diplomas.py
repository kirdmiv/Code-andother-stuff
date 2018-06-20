def get_cop(n, x, y):
    return n / x + n / y


def bin_search(num, x, y):
    left, right = 0, num * max(x, y) + 1
    while left + 1 != right:
        middle = (left + right) // 2
        if get_cop(middle, x, y) < 2:
            left = middle
        else:
            right = middle
        print(left, right, middle)
    return right



#def diplomas(n, w, h):
#    ans = max(w * 1, h * n)
#    for k in range(2, n):
#        width = w * k + 1
#        high = h * (n // k)
#        res = max(width, high)
#        if res < ans:
#            ans = res
#    return ans

diplomas_in = open('diplomas.in', 'r')
diplomas_out = open('diplomas.out', 'w')

w, h, n = map(int, diplomas_in.readline().split())
diplomas_in.close()

print(bin_search(n, w, h), file=diplomas_out)p;