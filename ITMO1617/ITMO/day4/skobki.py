from collections import deque

lst = list(input())
queue = deque()
b = True
for i in lst:
    if i == '(' or i == '[' or i == '{':
        queue.append(i)
    else:
        if queue == deque([]):
            b = False
            break
        last = queue.pop()
        if i == ')' and last != '(':
            b = False
            break
        if i == ']' and last != '[':
            b = False
            break
        if i == '}' and last != '{':
            b = False
            break
if b and queue == deque([]):
    print('yes')
else:
    print('no')
