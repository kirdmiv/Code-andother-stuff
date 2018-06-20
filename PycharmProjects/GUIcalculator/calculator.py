def sqrtx(x):
    return math.sqrt(x)


def fact(x):
    return math.factorial(x)


def truncx(x):
    return math.trunc(x)


def divison(x):
    x = 1 / x
    return x


def muult(a, n):
    b = a
    n = int(n)
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


def cont(a, s, b):
    a = float(a)
    b = float(b)
    if s == '-':
        res = sub(a, b)
    elif s == '+':
        res = sum(a, b)
    elif s == '*':
        res = mult(a, b)
    elif s == '/':
        res = div(a, b)
    else:
        res = muult(a, b)
    return res


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
    res = exp[i1]
    n = len(exp[i1:i2])
    if i2 == -1:
        i2 = n + 1
    i = i1 + 1
    while len(exp[i1:i2]) >= 3:
        res = cont(res, exp[i], exp[i + 1])
        del exp[i + 1]
        del exp[i]
        i2 -= 2
    exp[i1] = res
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


def calc(exp):
    b = True
    while b:
        i1, i2 = brackets(exp)
        if not i1 and not i2:
            res = count(exp, 0, -1)
            return res
        res = count(exp, i1, i2 - 1)
    return res


def calculator(exp2):
    try:
        global exp
        exp = list2(exp2)
        res = calc(exp)
        intres = int(res)
        if intres == res:
            return intres
        else:
            return res
    except:
        return 'Error'


import math
#print(calculator('( 55 - 3 ) - ( 32 + 20 )'))
#print(calculator('2 ^ 3'))