a, b = list(map(int, input().split()))
days = a // b
last_dinner = a % b
print(days, last_dinner)
