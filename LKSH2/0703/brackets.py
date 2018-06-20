def brackets():
    balance = 0
    min_bal = 0
    min_cnt = 0

    for i in string:
        if i == '(':
            balance += 1
        else:
            balance -= 1
        if min_bal == balance:
            min_cnt += 1
        if balance < min_bal:
            min_bal = balance
            min_cnt = 1
    if balance != 0:
        return 0
    return min_cnt


brackets_in = open('brackets.in', 'r')
brackets_out = open('brackets.out', 'w')

# Читаем
string = brackets_in.readline().rstrip()
brackets_in.close()

print(brackets(), file=brackets_out)
brackets_out.close()
