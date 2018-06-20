import sys

limit = 10 ** 9
sys.setrecursionlimit(limit)


def power(a, b, m, start_a, start_b, start_res):
    if b == 1:
        return a
    if a == 0:
        return 0
    a *= start_a
    a %= m
    if a == start_res:
        res = start_b - b - 1
        return power(a, res, m, start_a, start_b, start_res)
    if b == start_b:
        start_res = a
    return power(a, b - 1, m, start_a, start_b, start_res)


power_in = open('power.in', 'r')
power_out = open('power.out', 'w')

a, b, m = map(int, power_in.readline().split())
power_in.close()

start_a = a % m
start_b = b % m
ans = power(start_a, start_b, m, start_a, start_b, -100)
power_out.write(str(ans))

power_out.close()
