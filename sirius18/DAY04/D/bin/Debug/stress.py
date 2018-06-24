import random
import os

while 1:
    a, b = random.randint(0, 10 ** 6), random.randint(0, 10 ** 6)
    f = open('stress.in', 'w')
    print(a, b, file=f, sep='\n', end='')
    f.close()
    os.system('D.exe')
    f = open('stress.out')
    gg = f.readline().rstrip()
    f.close()
    if str(a - b) != gg:
        print(a, b)
        print(gg)
        print(a - b)
        input()
    else:
        print('passed')
