ejudge_in = open('ejudge.in', 'r')
ejudge_out = open('ejudge.out', 'w')
lst = []

# Читаем
n = int(ejudge_in.readline())
for i in range(5):
    tmp = list((map(int, ejudge_in.readline().split())))
    tmp[1] = 0 - tmp[1]
    tmp.append(-i)
    lst.append(tmp)
ejudge_in.close()

lst.sort(reverse=True)
for i in lst:
    print(abs(i[2]) + 1, file=ejudge_out, end=" ")
ejudge_out.close()
