import sys
sys.setrecursionlimit(10**9)

def rec(k, d, asafa):
    if k == 0:
        return asafa
    return max(rec(k-1, 0, asafa), rec(k-1, d+1, asafa+a[d % n]))


n, m = map(int, input().split())
a = list(map(int, input().split()))

print(rec(m, 0, 0))