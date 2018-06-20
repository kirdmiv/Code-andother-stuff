def from_edge(n, lst):
    new_lst = [[] for i in range(n)]
    for i in lst:
        j = i[0] - 1
        k = i[1] - 1
        new_lst[j].append(k)
        new_lst[k].append(j)
    return new_lst


def complete(lst):
    for i in lst:
        used = [False] * len(lst)
        for j in i:
            used[j] = True
        if used.count(False) > 1:
            return 'NO'
    return 'YES'


complete_in = open('complete.in', 'r')
complete_out = open('complete.out', 'w')

n, m = map(int, complete_in.readline().split())
lst = []
for i in range(m):
    lst.append(list(map(int, complete_in.readline().split())))
complete_in.close()

lst = from_edge(n, lst)
print(complete(lst), file=complete_out)
complete_out.close()
