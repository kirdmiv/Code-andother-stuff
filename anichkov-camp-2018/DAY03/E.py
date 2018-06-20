INF = 10 ** 9 + 7

fin = open("drill.in", 'r')
fout = open("drill.out", 'w')

n, m = map(int, fin.readline().split())
lst1 = list(map(int, fin.readline().split()))
lst2 = list(map(int, fin.readline().split()))

i = 0
j = 0
ans = INF
while i < n:
    res = INF
    while j < m:
        res = min(res, abs(lst1[i] - lst2[j]))
        if lst2[j] == lst1[i]:
            print(0, file=fout)
            exit()
        if abs(lst1[i] - lst2[j]) > res:
            j -= 1
            break
        j += 1
    ans = min(ans, res)
    i += 1

print(ans, file=fout)
fin.close()
fout.close()