fin = open("merlin.in", 'r')
fout = open("merlin.out", 'w')

n = int(fin.readline().rstrip())
a = list(map(int, fin.readline().split()))
a.sort()
pref = [0] * n
suff = [0] * n
suff[-1] = a[-1]
for i in range(1, n):
    pref[i] = pref[i-1] + (a[i] - a[i-1]) * i
    suff[n-i-1] = suff[n-i] + a[n-i-1]

#print(pref, suff, a)
if pref[-1] == 0:
    print(0, file=fout)
    exit()
for i in range(n-1, 0, -1):
    if pref[i - 1] <= suff[i]:
        print(n-i, file=fout)
        break
fin.close()
fout.close()