def segments(lst, lst_dots):
    res = [0] * len(lst_dots)
    for i in range(len(lst_dots)):
        for j in range(len(lst)):
            if lst[j][0] >= lst_dots[i]:
                break
        for k in range(len(lst) - 1, -1, -1):
            if lst[k][1] <= lst_dots[i]:
                break
            if k == 0:
                j += 1
        print(lst, lst_dots, j, k)
        res[i] = j - k
    return res


segments_in = open('segments.in', 'r')
segments_out = open('segments.out', 'w')

n, m = map(int, segments_in.readline().split())
lst = []
for i in range(n):
    a, b = map(int, segments_in.readline().split())
    a, b = min(a, b), max(a, b)
    lst.append([a, b])
lst.sort()

lst_dots = list(map(int, segments_in.readline().split()))
segments_in.close()

print(*segments(lst, lst_dots), file=segments_out)
segments_out.close()
