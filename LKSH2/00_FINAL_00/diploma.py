INF = 10 ** 9


def bin_solution(mid):
    return (mid // w) * (mid // h)


def bin_search():
    left = 0
    right = max(w, h) * n
    while right - left > 1:
        mid = (right + left) // 2
        if bin_solution(mid) < n:
            left = mid
        else:
            right = mid
    return right


# Читаем
w, h, n = map(int, input().split())

ans = bin_search()
print(ans)