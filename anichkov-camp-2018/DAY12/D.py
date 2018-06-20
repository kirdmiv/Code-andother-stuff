n = int(input())
s = input()
pref = [0]
suf = [0]
for i in range(n):
    pref.append(pref[i])
    if s[i] == 'e':
        pref[-1] += 1
for i in range(n):
    suf.append(suf[i])
    if s[n - 1 - i] == 't':
        suf[-1] += 1
best = suf[n]
bestT = 0
for T in range(n + 1):
    if pref[T] + suf[n - T] < best:
        best = pref[T] + suf[n - T]
        bestT = T
print(best)
print("t" * bestT + "e" * (n - bestT))
