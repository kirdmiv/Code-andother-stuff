s = input()

cnt = 0
prev = ''
for i in range(len(s)):
    if prev == '-' and (i < 2 or s[i - 2] == ',' or s[i - 2] == '.' or s[i - 2] == ' ' or s[i - 2] == '!' or s[i - 2] == '?') and (s[i] != '.' and s[i] != ',' and s[i] != '.' and s[i] != ' ' and s[i] != '!' and s[i] != '?' and s[i] != '-'):
        cnt += 1
    elif (prev == '' or prev == '.' or prev == ',' or prev == '.' or prev == ' ' or prev == '!' or prev == '?') and (s[i] != '.' and s[i] != ',' and s[i] != '.' and s[i] != ' ' and s[i] != '!' and s[i] != '?' and s[i] != '-'):
        cnt += 1
    prev = s[i]
print(cnt)