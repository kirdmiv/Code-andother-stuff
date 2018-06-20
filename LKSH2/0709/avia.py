import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)


avia_in = open('avia.in', 'r')
avia_out = open('avia.out', 'w')

n, s, f = map(int, avia_in.readline().split())
graph = []
for i in range(n):
    graph.append(list(map(int, avia_in.readline().split())))
avia_in.close()

graph = mtoal(graph, n)
way_to_finish = avia(graph, s - 1, f - 1)
if way_to_finish == None:
    print(0, file=avia_out)
else:
    print(way_to_finish, file=avia_out)
avia_out.close()
