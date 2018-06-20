from collections import deque
queue_in = open('queue.in', 'r')
queue_out = open('queue.out', 'w')

queue = deque()
n = int(queue_in.readline())
for i in range(n):
    tmp = queue_in.readline().split()
    if tmp[0] == '-':
        print(queue.popleft(), file=queue_out)
    else:
        queue.append(tmp[1])
queue_in.close()
queue_out.close()