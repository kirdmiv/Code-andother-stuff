def min_cover():
    res = 0
    res_lst = []
    curent = 0
    while res < m:

        dot = -1
        segment = (-1, -1)

        while curent < len(segments) and segments[curent][0] <= res:
            if segments[curent][1] > dot:
                dot = segments[curent][1]
                segment = segments[curent]
            curent += 1

        if dot == -1:
            return "No solution", []
        else:
            res_lst.append(segment)
        res = dot
    return len(res_lst), res_lst


cover_in = open('cover.in', 'r')
cover_out = open('cover.out', 'w')

# Читаем
segments = []
m = int(cover_in.readline())
left, right = list(map(int, cover_in.readline().split()))
while (left != 0) or (right != 0):
    segments.append((left, right))
    left, right = list(map(int, cover_in.readline().split()))
cover_in.close()
segments.sort()

ans, ans_list = min_cover()

print(ans, file=cover_out)
if ans != "No solution":
    for i in range(ans):
        print(*ans_list[i], file=cover_out)
cover_out.close()
