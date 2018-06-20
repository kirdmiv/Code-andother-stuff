def check(x):
    cnt = 0
    for i in range(n):
        cnt += a[i] // x
        if cnt >= k:
            return True
    return False


def bsearch():
    left = 0
    right = inf + 1
    for i in range(100):
        middle = (left + right) / 2
        if check(middle):
            left = middle
        else:
            right = middle
    return left


#n - изначальное количество палочек; k - количество сторон k-угольника
n, k = map(int, input().split())
#a - массив длин палочек
a = list(map(float, input().split()))
inf = max(a)
print(bsearch())
