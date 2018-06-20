fin = open("biology.in", 'r')
fout = open("biology.out", 'w')

s = fin.readline().rstrip()
t = fin.readline().rstrip()

l = len(s)
j = 0
for i in range(len(t)):
    if t[i] == s[j]:
        j += 1
    if j == l:
        print("YES", file=fout)
        exit()
print("NO", file=fout)

fin.close()
fout.close()