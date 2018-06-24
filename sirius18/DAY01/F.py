d, m = map(int, input().split())
if m > 1:
    d += 31
if m > 2:
    d += 28
if m > 3:
    d += 31
if m > 4:
    d += 30
if m > 5:
    d += 31
if m > 6:
    d += 30
if m > 7:
    d += 31
if m > 8:
    d += 31
if m > 9:
    d += 30
if m > 10:
    d += 31
if m > 11:
    d += 30
print(d)


