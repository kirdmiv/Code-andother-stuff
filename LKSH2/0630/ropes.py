def binsol(length):
    res = 0
    for i in lst:
        res += i // length
    return res >= ropes


ropes_in = open('ropes.in', 'r')
ropes_out = open('ropes.out', 'w')
lst = []

# Читаем
n, ropes = map(int, ropes_in.readline().split())
for i in range(n):
    lst.append(int(ropes_in.readline()))
ropes_in.close()

left = 0
right = sum(lst)

while right - left != 1:
    mid = (right + left) // 2
    if binsol(mid):
        left = mid
    else:
        right = mid
print(left, file=ropes_out)
ropes_out.close()
