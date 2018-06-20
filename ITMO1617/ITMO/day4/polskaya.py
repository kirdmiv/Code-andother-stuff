import operator


def calc(expr):
    OPERATORS = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    stack = [0]
    for i in expr.split(" "):
        if i in OPERATORS:
            op2, op1 = stack.pop(), stack.pop()
            stack.append(OPERATORS[i](op1, op2))
        elif i:
            stack.append(int(i))
    return stack.pop()


str = input()
print(calc(str))
