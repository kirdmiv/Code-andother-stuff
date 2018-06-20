from collections import deque
def necklace(lst):
    lst = deque(lst)
    a = 0
    i = 0





def necklace(lst):
    lst = deque(lst)
    a = 0
    i = 0
    while i < 10:
        print(lst)
        if a == 0:
            a = lst.popleft()
        b = lst[0]
        c = lst[-1]
        if a < c and a < b:
            lst.append(a)
            print('MR')
            a = 0
        elif b < a < c:
            lst.append(lst.popleft())
            print('RL')
            print('MR')
        else:
            if a < b:
                lst.append(a)
                print('MR')
                a = 0
            else:
                lst.append(lst.popleft())
                print('RL')
                print('MR')
        i += 1


necklace_in = open('necklace.in', 'r')
necklace_out = open('necklace.out', 'w')

n = int(necklace_in.readline())
lst = list(map(int, necklace_in.readline().split()))
necklace_in.close()

necklace(lst)
necklace_out.close()
