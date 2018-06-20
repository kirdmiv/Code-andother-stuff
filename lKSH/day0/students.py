s = input()
n = len(s)
if s[-1] == 's':
    if n != 1:
        s += s[-2:]
        n += 2
    else:
        s = 'ss'
        n += 1
if n > 10:
    s += s
print(s)