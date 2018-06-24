import random
import os

while 1:
    a, b = random.randint(0, 10 ** 18), random.randint(0, 10 ** 18)
    f = open('stress.in', 'w')
    print(a, b, file=f, sep='\n', end='')
    f.close()
    os.system('F.exe')
    f = open('stress.out')
    gg = f.readline().rstrip()
    f.close()
    if str(a // b) != gg:
        print(a, b)
        print(gg)
        print(a // b)
        input()
    else:
        print('passed')
