n = int(input())
cnt = 1
while (n%2==0 and n > 2):
    n//=2
cnt += n-1
print(cnt)