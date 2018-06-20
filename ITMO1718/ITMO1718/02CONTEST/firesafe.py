def main():
    ans = []
    for i in range(len(lst)):
        if lst[i] == []:
            ans.append(i + 1)
    if ans == []:
        ans = [1]
    return ans


fin = open("firesafe.in", 'r')
fout = open("firesafe.out", 'w')

n = int(fin.readline())
m = int(fin.readline())
lst = [[] for i in range(n)]
for i in range(m):
    k, j = map(int, fin.readline().split())
    if not (j - 1 in lst[k - 1]):
        lst[k - 1].append(j - 1)

ans = main()
print(len(ans), file=fout)
for i in ans:
    print(i, file=fout)
fout.close()
fin.close()
