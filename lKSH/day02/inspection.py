def minimum(a):
    min1 = min2 = 10 ** 10
    for i in a:
        if i <= min1:
            min1, min2 = i, min1
        elif i < min2:
            min2 = i
    return min1, min2


inspin = open('inspection.in', 'r')
inspout = open('inspection.out', 'w')

n = inspin.readline()
drone_nums = list(map(int, inspin.readline().split()))
inspin.close()

res = minimum(drone_nums)
ans = [str(i) for i in res]
ans = ' '.join(ans)
inspout.write(ans)
inspout.close()
