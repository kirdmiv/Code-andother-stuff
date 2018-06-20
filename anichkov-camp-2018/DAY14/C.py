import math

fin = open("locker.in", 'r')
fout = open("locker.out", 'w')

s = fin.readline().rstrip()
res = 0
res2 = []
for i in range(len(s)//2):
    if s[i] != s[-i-1]:
        res += 1
        res2.append(i)

#print(s, res, res2)
#print(res)
if res == 0:
    print("YES", file=fout)
elif res == 1:
    if (len(s)%2 == 1) and ((s[len(s)//2] == s[res2[0]]) or (s[len(s)//2] == s[-res2[0]-1])):
        print("YES", file=fout)
        #print(s[len(s)//2], s[res2[0]], s[len(s)//2], s[-res2[0]-1])
    else:
        print("NO", file=fout)
elif res == 2:
    if (s[res2[0]] == s[-res2[1]-1] and s[res2[1]] == s[-res2[0]-1]) or \
            (s[res2[0]] == s[res2[1]] and s[-res2[0]-1] == s[-res2[1]-1]):
        print("YES", file=fout)
    else:
        print("NO", file=fout)
else:
    print("NO", file=fout)
fin.close()
fout.close()
