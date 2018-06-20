SAND = 500
sand = SAND
permutations = list(map(int, input().split()))
try:
    j = 0
    for i in range(2):
        sand = sand / permutations[j] * permutations[j + 1]
        j += 2
    res = SAND / permutations[-1] * permutations[-2]
    if res >= sand:
        print('Hermione')
    else:
        print('Ron')
except ZeroDivisionError:
    print('Hermione')
