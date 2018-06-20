import sys

sys.setrecursionlimit(10 ** 9)


def calc(n, k):
    if k == 0:
        print(n, file=calc_out)
        return
    calc(n + 1, k - 1)
    calc(n * 3, k - 1)


calc_in = open('calc.in', 'r')
calc_out = open('calc.out', 'w')

n, k = map(int, calc_in.readline().split())
calc_in.close()

calc(n, k)
calc_out.close()
