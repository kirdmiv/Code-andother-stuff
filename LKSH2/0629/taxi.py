taxi_in = open('taxi.in', 'r')
taxi_out = open('taxi.out', 'w')

# Читаем
n = int(taxi_in.readline())
km = list(map(int, taxi_in.readline().split()))
price = list(map(int, taxi_in.readline().split()))
taxi_in.close()

km2 = []
for i in range(len(km)):
    km2.append([km[i], i])
km2.sort()

price2 = []
for i in range(len(price)):
    price2.append([price[i], i])
price2.sort(reverse=True)

ans = [0] * n

for i in range(n):
    tmp_km = km2[i][1]
    tmp_price = price2[i][1]
    ans[tmp_km] = tmp_price

for i in ans:
    print(i + 1, file=taxi_out, end=" ")
taxi_out.close()