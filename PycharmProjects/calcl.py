def divison(x):
    x = 1 / x
    return x


def muult(a, n):
    b = a
    for i in range(n - 1):
        a *= b
    return a

def list2(exp):
    n = len(exp)
    k2 = 0
    for s in exp:
        if s == ' ':
            k2 += 1
    k = 0
    i = 0
    L = [0] * (k2 + 1)
    while i < n:
        s = ''
        ii = i
#        i -= 1
        while ii < n and exp[ii] != ' ':
            ii += 1
        s = exp[i:ii]
        i = ii
        L[k] = s
        i += 1
        k += 1
    return L


def sum(a, b):
    return a + b


def sub(a, b):
    return a - b


def mult(a, b):
    return a * b


def div(a, b):
    if a % b == 0:
        return a // b
    return a / b


def exp_to_str(a):
    s = ''
    for i in a:
        s += str(i)
        s += ' '
    s = s[:-1]
    return s


def check_sign(c):
    if c == '+':
        return
    if c == '-':
        return
    if c == '*':
        return
    if c == '/':
        return
    if c == '(':
        return
    if c == ')':
        return
    else:
        print('Error')
        exit()


def sings(a):
    si = []
    for i in range(1, len(a), 2):
        check_sign(a[i])
        si += a[i]
    return si


def check_num(a):
    z = ['-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for it in range(len(a)):
        for itz in range(len(z)):
            if a[it] == z[itz]:
                break
            if itz == 10:
                print('Error')
                exit()
    return


def numbers(a):
    L = len(a)
    k = 0
    num = [0] * round(L / 2)
    for i in range(0, L, 2):
        check_num(a[i])
        ai = int(a[i])
        num[k] += ai
        k += 1
    return num


def cont(a, s, b):
    a = int(a)
    b = int(b)
    if s == '-':
        res = a - b
    elif s == '+':
        res = a + b
    elif s == '*':
        res = a * b
    elif s == '/':
        res = a / b
        if res == a // b:
            res = round(res)
    else:
        res = a ** b
    return res


def brackets(exp):
    for i in range(len(exp)):
        if exp[i] == ')':
            for it in range(i, -1, -1):
                if exp[it] == '(':
                    del exp[i]
                    del exp[it]
                    return it, i
            return False, False
    return False, False

def count(exp, i1, i2):
    i3 = i2
    i = i1 + 1
    while i1 + 1 <= i <= i2 - 1:
        s = exp[i]
        if s == '*' or s == '/' or s == '^':
            exp[i] = cont(exp[i - 1], s, exp[i + 1])
            del exp[i + 1]
            del exp[i - 1]
            i2 -= 2
            i -= 2
        i += 2
    res = exp[0]
    n = len(exp[i1:i2])
    for i in range(i1 + 1, n - 1, 2):
        res = cont(res, exp[i], exp[i + 1])
        del exp[i]
        del exp[i + 1]
        return res


def calc(exp):
    b = True
    while b:
        i1, i2 = brackets(exp)
        if i1 == False:
            res = count(exp, 0, -1)
        return res
	res = count(exp, i1, i2)


def calculator(exp2):
    global exp
    exp = list2(exp2)
    n = len(exp)
    res = calc(exp)
    return res


print(calculator('234 - 66'))
#brackets(['(', '234', ')', '3'])