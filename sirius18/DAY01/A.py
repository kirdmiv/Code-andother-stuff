n = int(input())
m = int(input())
k = int(input())

ans = 0
while m > 0:
    m -= k//n
    ans += 1
print(ans)