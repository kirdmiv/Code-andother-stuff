arrival_in = open('arrival.in', 'r')
arrival_out = open('arrival.out', 'w')

# Читаем
n, m = map(int, arrival_in.readline().split())
lst = list(map(int, arrival_in.readline().split()))
arrival_in.close()

lst2 = []
for i in range(len(lst)):
    lst2.append([lst[i], i + 1])
lst2.sort(reverse=True)
res = 0
ans = []
check = False
for i in range(len(lst)):
    res += lst2[i][0]
    ans.append(lst2[i][1])
    if res >= n:
        check = True
        break
if check:
    ans.reverse()
    print(len(ans), file=arrival_out)
    for i in ans:
        print(i, file=arrival_out, end=" ")
else:
    print(-1, file=arrival_out)
arrival_out.close()
