def erase():
    lst = ['']
    dictionary = {'}': '{', ')': '(', ']': '['}
    for i in string:
        if i in ['}', ']', ')'] and lst[-1] == dictionary[i]:
            lst.pop()
        else:
            lst.append(i)
    return lst


erase_in = open('erase2.in', 'r')
erase_out = open('erase2.out', 'w')

# Читаем
string = erase_in.readline().rstrip()
erase_in.close()

print(*erase(), file=erase_out)
erase_out.close()
