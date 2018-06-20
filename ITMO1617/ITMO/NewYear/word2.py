mainstring = input()
n = int(input())
lst = []
for i in range(n):
    lst.append(input())
res = ''
j = 0
while j < len(mainstring):
    for string in lst:
        tmp = len(string)
        if mainstring[j:tmp + j] == string:
            res += string
            res += " "
            j += tmp
print(res)
