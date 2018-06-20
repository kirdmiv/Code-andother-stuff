def check():
    lst = ['']
    dictionary = {'}': '{', ')': '(', ']': '['}
    for i in string:
        if i in ['}', ']', ')']:
            if lst[-1] == dictionary[i]:
                lst.pop()
            else:
                return "NO"
        else:
            lst.append(i)
    if len(lst) > 1:
        return "NO"
    return "YES"


check_in = open('check.in', 'r')
check_out = open('check.out', 'w')

# Читаем
string = check_in.readline().rstrip()
check_in.close()

print(check(), file=check_out)
check_out.close()
