h1, m1, h2, m2 = map(int, input().split())

cnt = 0
#lol
while h1 != h2 or m1 != m2:
    #print(h1, m1)
    if m1 == 30:
        cnt += 1
    if m1 == 0:
        cnt += h1
    m1 += 1
    if m1 == 60:
        h1 += 1
        m1 = 0
print(cnt)