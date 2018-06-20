def erase():
    lst = ['']
    for i in string:
        if i == ')' and lst[-1] == '(':
            lst.pop()
        else:
            lst.append(i)
    return len(lst) - 1


erase_in = open('erase.in', 'r')
erase_out = open('erase.out', 'w')

# Читаем
string = erase_in.readline().rstrip()
erase_in.close()

print(erase(), file=erase_out)
erase_out.close()
