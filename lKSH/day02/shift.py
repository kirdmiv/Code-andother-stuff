def shift(a):
    for i in range(len(a)):
        a[i], a[-1] = a[-1], a[i]
    return a


shiftin = open('shift.in', 'r')
shiftout = open('shift.out', 'w')

n = shiftin.readline()
nums = list(map(int, shiftin.readline().split()))
shiftin.close()

res = shift(nums)
ans = [str(i) for i in res]
ans = ' '.join(ans)
shiftout.write(ans)
shiftout.close()