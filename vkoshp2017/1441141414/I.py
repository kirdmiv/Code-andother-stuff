import random

fin = open("sochi.in", "r")
fout = open("sochi.out", "w")

n, d = map(int, fin.readline().split())
a = list(map(int, fin.readline().split()))

def sol2(n, d, a):
    a.sort(reverse=True)
    tmp1 = a[0]

    ans = tmp1
    f = False
    for i in range(1, n):
        if f:
            break
        if a[i] < d + d + d:
            f = True
        tmp1 += a[i] - d - d
        if tmp1 <= ans:
            break
        else:
            ans = tmp1

    return ans

    fin.close()
    fout.close()

def sol1(n, d, a):
    a.sort(reverse=True)
    ans = a[0]
    left = 0
    right = 0
    cur = True
    for i in range(1, n):
        if cur:
            if a[i] > 2 * d and a[right] >= 2 * d:
                ans += a[i] - d - d
                a[right] -= d
                a[i] -= d
                right = i
        else:
            if a[i] > 2 * d and a[left] >= 2 * d:
                ans += a[i] - d - d
                a[left] -= d
                a[i] -= d
                left = i
        cur = not cur

    return ans



    fin.close()
    fout.close()


for n in range(1, 21):
    a = []
    for i in range(n):
        a.append(random.randint(1, 100))
    d = random.randint(1, 20)
    res1 = sol2(n, d, a.copy())
    res2 = sol1(n, d, a.copy())
    if res1 != res2:
        print(n, d, a, res1, res2)