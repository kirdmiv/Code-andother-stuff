def segments(lst, lst_dots):
    res = [0] * len(lst_dots)
    for i in range(len(lst_dots)):
        for j in lst:
            if j[0] <= lst_dots[i] <= j[1]:
                res[i] += 1
            elif res[i] > 0:
                break
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
