from functools import cmp_to_key


def sort_key(a, b):
    if (a + b) > (b + a):
        return 1
    elif (a + b) == (b + a):
        return 0
    else:
        return -1


number_in = open('number.in', 'r')
number_out = open('number.out', 'w')

# Читаем
lst = []
tmp = True
while tmp != "":
    tmp = number_in.readline().rstrip()
    lst.append(tmp)
number_in.close()
lst.sort(key=cmp_to_key(sort_key), reverse=True)
print(*lst, file=number_out, sep='')

number_out.close()
