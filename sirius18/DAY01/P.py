s = input()

n = len(s)
cnt = (0, 0, 0)
for i in range(n):
    if s[i] == '(':
        cnt[0] += 1
    if s[i] == '{':
        cnt[1] += 1
    if s[i] == '[':
        cnt[2] += 1
    