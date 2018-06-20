lst = input().split()
i = 0
while i < len(lst):
    if lst[i] == '+':
        lst = lst[:i - 2] + [int(lst[i - 2]) + int(lst[i - 1])] + lst[i + 1:]
        i -= 1
    elif lst[i] == '-':
        lst = lst[:i - 2] + [int(lst[i - 2]) - int(lst[i - 1])] + lst[i + 1:]
        i -= 1
    elif lst[i] == '*':
        lst = lst[:i - 2] + [int(lst[i - 2]) * int(lst[i - 1])] + lst[i + 1:]
        i -= 1
    else:
        i += 1
print(lst[0])
