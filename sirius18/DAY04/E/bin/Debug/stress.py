import random
import os

while 1:
    a, b = random.randint(0, 10 ** 2500), random.randint(0, 10 ** 6)
    f = open('stress.in', 'w')
    print(a, b, file=f, sep='\n', end='')
    f.close()
    os.system('E.exe')
    f = open('stress.out')
    gg = f.readline().rstrip()
    hh = f.readline().rstrip()
    f.close()
    if str(a // b) != gg or str(a % b) != hh:
        print(a, b)
        print(gg)
        print(hh)
        print(a // b, a % b)
        input()
    else:
        print('passed')
