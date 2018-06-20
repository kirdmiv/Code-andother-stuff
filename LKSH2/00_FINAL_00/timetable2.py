def min_timetable():
    res = 0
    res_lst = []
    curent = 0
    while segments[-1][1]:

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


timetable_in = open('timetable.in', 'r')
timetable_out = open('timetable.out', 'w')

# Читаем
segments = []
n = int(timetable_in.readline())
segments = [[-1, -1, -1]]
for i in range(n):
    tmp = list(map(int, timetable_in.readline().split()))
    segments.append([tmp[0], tmp[1], i])
segments.sort()

timetable_in.close()

ans, ans_list = min_timetable()

print(ans, file=timetable_out)
if ans != "No solution":
    for i in range(ans):
        print(*ans_list[i], file=timetable_out)
timetable_out.close()
