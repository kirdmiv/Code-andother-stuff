import bisect


def bin_solution(mid, x, right):
    return cities[mid][0] < x or (cities[mid][0] == x and cities[mid][1] <= right)


def bin_search(x):
    left = 0
    right = n
    while left < right:
        mid = (right + left) // 2
        if cities[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left


def solution(question):
    left = bin_search((question[2], question[0]))
    if left < n and (cities[left][0] == question[2]) and (question[0] <= cities[left][1] <= question[1]):
        return "1"
    return "0"


queries_in = open('queries.in', 'r')
queries_out = open('queries.out', 'w')

# Читаем
n = int(queries_in.readline())
lst = list(map(int, queries_in.readline().split()))

cities = []
for i in range(len(lst)):
    cities.append((lst[i], i + 1))
cities.sort()

ans = ""
num = int(queries_in.readline())
for j in range(num):
    tmp = list(map(int, queries_in.readline().split()))
    ans += solution(tmp)

print(ans, file=queries_out)
queries_in.close()
queries_out.close()
