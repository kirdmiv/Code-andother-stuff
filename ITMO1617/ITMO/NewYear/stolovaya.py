n, m = map(int, input().split())
lst = []
for i in range(m):
    lst.append(list(map(int, input().split())))
new_lst = [[0] * n for i in range(n)]
for i in lst:
    s = i[0] - 1
    e = i[1] - 1
    l = i[2]
    if l > new_lst[s][e]:
        new_lst[s][e] = l
    if l > new_lst[e][s]:
        new_lst[e][s] = l
num_lst = [0] * n
for i in range(len(new_lst)):
    num_lst[i] = new_lst[i].count(0)
min = num_lst[0]
min_index = [0]
for i in range(1, len(num_lst)):
    if num_lst[i] == min:
        min_index.append(i)
    if num_lst[i] < min:
        min = num_lst
        min_index = [i]
sum_lst = [0] * n
for i in range(len(new_lst)):
    num_lst[i] = sum(new_lst[i])
if len(min_index) > 1:
    min_lst = []
    for i in min_index:
        