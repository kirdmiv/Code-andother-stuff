def push(n):
    queue.append(n)
    return


def popelem():
    if queue == deque([]):
        return 'error'
    return queue.pop()


def size():
    return len(queue)


def back():
    if queue == deque([]):
        return 'error'
    return queue[-1]


def clear():
    while True:
        try:
            queue.pop()
        except:
            break


from collections import deque

queue = deque()
while True:
    commands = input().split()
    if commands[0] == 'push':
        push(int(commands[1]))
        print('ok')
    elif commands[0] == 'pop':
        print(popelem())
    elif commands[0] == 'back':
        print(back())
    elif commands[0] == 'size':
        print(size())
    elif commands[0] == 'clear':
        clear()
        print('ok')
    elif commands[0] == 'exit':
        print('bye')
        break
