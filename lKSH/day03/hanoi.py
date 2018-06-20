import sys

sys.setrecursionlimit(1000000)


def hanoi(n, source, to, middle):
    if n == 1:
        print(source, to, file=hanoi_out)
    else:
        hanoi(n - 1, source, middle, to)
        print(source, to, file=hanoi_out)
        hanoi(n - 1, middle, to, source)


hanoi_in = open('hanoi.in', 'r')
hanoi_out = open('hanoi.out', 'w')

n = int(hanoi_in.readline())
hanoi_in.close()

hanoi(n, 1, 2, 3)

hanoi_out.close()
