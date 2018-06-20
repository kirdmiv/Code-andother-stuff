n = int(input())
ans = ''

for i in range(n):
    ans += input()[::-1]
print(ans[::-1])
