import sys
sys.setrecursionlimit(1000000)


def two(n, k=1):
    if k > n:
        return "NO"
    elif n == k:
        return "YES"
    return two(n, k * 2)


two_in = open('two.in', 'r')
two_out = open('two.out', 'w')

n = int(two_in.readline())
two_in.close()

ans = two(n)
two_out.write(ans)

two_out.close()
