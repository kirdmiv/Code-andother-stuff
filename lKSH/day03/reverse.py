import sys

sys.setrecursionlimit(1000000)


def reverse_lst(n, k=1):
    num = reverse_in.readline().strip()
    if k > n:
        return ''
    rev = reverse_lst(n, k=k + 1)
    if k > n:
        return num
    return rev + ' ' + num


reverse_in = open('reverse.in', 'r')
reverse_out = open('reverse.out', 'w')

n = int(reverse_in.readline())

ans = reverse_lst(n)
reverse_out.write(ans)

reverse_out.close()
reverse_out.close()
