str_text, lenth = list(map(int, input().split()))
n = input()
customers = list(map(int, input().split()))
for i in range(len(customers)):
    str_text -= customers[i] * lenth
    if str_text < 0:
        print(i)
        break
else:
    print(n)
