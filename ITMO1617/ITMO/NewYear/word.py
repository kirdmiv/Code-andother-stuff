mainstring = input()
n = int(input())
lst = []
for i in range(n):
    lst.append(input())
res = ''
j = 0
while j < len(mainstring):
    for i in range(j, len(mainstring) + 1):
        if mainstring[j:i] in lst:
            res += mainstring[j:i]
            res += " "
            j = i
print(res)
