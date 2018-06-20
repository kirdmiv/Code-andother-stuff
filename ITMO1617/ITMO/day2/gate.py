n, w = map(int, input().split())
start, end = map(int, input().split())
lst = list(map(int, input().split()))
start_lst = str(lst)
lst.sort()
lst = [start] + lst + [end]
i = 0
j = n - 1
res = lst[1:n - 1]
while i < n and j < 0:
    if lst[j] - lst[i] < w:
        if res == []:
            print(-1)
            exit()
        break
    elif lst[j] - lst[i] >= w:
        res = lst[i:j]
        j -= 1
print(len(res))
for i in range(len(res)):
    ans = start_lst.find(str(res[i])) - 1
    print(ans)
