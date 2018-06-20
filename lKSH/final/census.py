census_in = open('census.in', 'r')
census_out = open('census.out', 'w')

n = int(census_in.readline())
lst = list(map(int, census_in.readline().split()))
lst.sort()
max_res = 1
change = 1
for i in range(n - 1, -1, -1):
    if change:
        res = 1
    if lst[i] == lst[i - 1]:
        res += 1
        change = 0
    else:
        change = 1
    if res >= max_res:
        ans = lst[i]
        max_res = res
print(ans, file=census_out)
census_in.close()
census_out.close()
