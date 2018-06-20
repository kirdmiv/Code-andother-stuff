fin = open(".in", 'r')
fout = open(".out", 'w')

s = fin.readline().rstrip()
n = len(s)
p = [0] * n
for i in range(1, n):
    j = p[i - 1]
    while j > 0 and s[i] != s[j]:
        j = p[j - 1]
    if s[i] == s[j]:
        j += 1
    p[i] = j

print(sum(p), file=fout)
fin.close()
fout.close()

'''
prefix
trans
inverse
pref
'''