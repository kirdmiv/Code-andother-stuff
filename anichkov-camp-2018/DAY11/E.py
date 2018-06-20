n = int(input())
a = list(map(int, input().split()))
ans = []
for i in range(n):
    ans.append((a[i], 0))

for i in range(n-2):
