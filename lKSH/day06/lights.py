lights_in = open('lights.in', 'r')
lights_out = open('lights.out', 'w')

n, m = map(int, lights_in.readline().split())
lst = [0] * n
for i in range(m):
    a, b = map(int, lights_in.readline().split())
    lst[a - 1] += 1
    lst[b - 1] += 1
lights_in.close()

print(' '.join([str(i) for i in lst]), file=lights_out)
lights_out.close()
