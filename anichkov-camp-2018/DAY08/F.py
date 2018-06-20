fin = open("indic.in", 'r')
fout = open("indic.out", 'w')

n, k = map(int, fin.readline().split())


ans1 = ['8'] * n
cur = 7 * n
if cur < k:
    print("NO SOLUTION", file=fout)
    exit()

if cur - k >= 1:
    cur -= 1
    ans1[0] = '6'

for i in range(1, n):
    if cur - k >= 1:
        cur -= 1
        ans1[i] = '0'

ukaz = -100
for i in range(n-1, 0, -1):
    if cur - k >= 4:
        cur -= 4
        ans1[i] = '1'
    else:
        ukaz = i
        break


if k == cur:
    pass
elif ukaz == -100:
    print("NO SOLUTION", file=fout)
    exit()
elif cur - k == 3:
    ans1[ukaz] = '7'
elif cur - k == 2:
    ans1[ukaz] = '4'
elif cur - k == 1:
    ans1[ukaz] = '2'
else:
    print("NO SOLUTION", file=fout)
    exit()



ans2 = ['8'] * n
cur = 7 * n
if cur < k:
    print("NO SOLUTION", file=fout)
    exit()

for i in range(n):
    if cur - k >= 1:
        cur -= 1
        ans2[i] = '9'
ukaz = -100
for i in range(n-1, -1, -1):
    if cur - k >= 4:
        cur -= 4
        ans2[i] = '1'
    else:
        ukaz = i
        break


if k == cur:
    pass
elif ukaz == -100:
    print("NO SOLUTION", file=fout)
    exit()
elif cur - k == 3:
    ans2[ukaz] = '7'
elif cur - k == 2:
    ans2[ukaz] = '4'
elif cur - k == 1:
    ans2[ukaz] = '5'
else:
    print("NO SOLUTION", file=fout)
    exit()



print(*ans1, sep="", file=fout)
print(*ans2, sep="", file=fout)


fin.close()
fout.close()
