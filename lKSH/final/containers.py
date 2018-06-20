def containers(n):
    containers = [[0] * 2 for i in range(n)]
    containers[0][0] = containers[0][1] = 1
    for i in range(1, n):
        containers[i][0] = containers[i - 1][1]
        containers[i][1] = containers[i - 1][0] + containers[i - 1][1]
    return sum(containers[n - 1])


containers_in = open('containers.in', 'r')
containers_out = open('containers.out', 'w')

n = int(containers_in.readline())
containers_in.close()

print(containers(n), file=containers_out)
containers_out.close()
