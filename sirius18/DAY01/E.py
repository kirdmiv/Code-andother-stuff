s = list(map(int, input().split()))
sum = 0
for i in range(len(s)):
    sum += s[i]
if sum % 3 == 0:
    print("YES")
else:
    print("NO")