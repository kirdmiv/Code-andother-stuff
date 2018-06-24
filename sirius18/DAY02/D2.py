import math

def smt(x, y):
    #print(x, y)
    sq = math.sqrt(x)
    d = []
    s = 1
    while s <= sq:
        if s == sq and s > y:
            d.append(s)
        elif x % s == 0:
            if s > y:
                d.append(s)
            if x // s > y:
                d.append(x // s)
        s += 1
    return d


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a



n = int(input())
maxy = 0
nums = [0] * n
for i in range(n):
    x, y = map(int, input().split())
    maxy = max(y, maxy)
    nums[i] = x - y

#print(nums)
res = nums[0]
for i in range(1, n):
    res = gcd(res, nums[i])

ans = smt(res, maxy)

print(len(ans))
print(*ans)