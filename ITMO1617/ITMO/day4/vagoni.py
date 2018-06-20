from collections import deque

n = int(input())
que1 = deque(list(map(int, input().split())))
que2 = deque()
que3 = deque()
res = [[1, 0]]
i = 0
min = 1
while que1 != deque([]):
    que2.append(que1[i])
    que1.popleft()
    if res[-1][0] == 1:
        j = res[-1][1]
        res[-1][1] = j + 1
    else:
        res.append([1, 1])
    if que2[-1] == min:
        que3.append(que2.pop())
        res.append([2, 1])
        min += 1
for i in range(len(que2) - 1, -1, -1):
    if que2[i] == min:
        que3.append(que2.pop())
        if res[-1][0] == 2:
            j = res[-1][1]
            res[-1][1] = j + 1
        else:
            res.append([2, 1])
        min += 1
if que2 == deque([]):
    for i in res:
        print(*i)
else:
    print(0)
