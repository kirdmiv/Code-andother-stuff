def rain(lst, colors):
    res = 0
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j]:
                if colors[i] != colors[j]:
                    res += 1
    return res // 2


rain_in = open('rain.in', 'r')
rain_out = open('rain.out', 'w')

n = int(rain_in.readline())
lst = [[]] * n
for i in range(n):
    lst[i] = list(map(int, rain_in.readline().split()))
colors = list(map(int, rain_in.readline().split()))
print(rain(lst, colors), file=rain_out)
rain_in.close()
rain_out.close()
