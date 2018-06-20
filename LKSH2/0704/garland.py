def garland():
    chars = {'d': 0, 'h': 0, 'u': 0}
#    chars = [0, 0, 0]
    for i in range(n - 1, -1, -1):
        if lst[i] == 'h':
    return 0




garland_in = open('garland.in', 'r')
garland_out = open('garland.out', 'w')

# Читаем
n = int(garland_in.readline())
lst = list(garland_in.readline().split())
#dp = [[0] * n for i in range(n)]
#dp[0][0] = 1
garland_in.close()

print(dp)
garland_out.close()
