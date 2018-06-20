import sys
sys.setrecursionlimit(10 ** 6)


def is_subseq(lst):
    res = ''
    len_res = 0
    for i in range(len(lst)):
        if lst[i]:
            res += str(i + 1) + ' '
            len_res += 1
    res = res[:-1]
    if res:
        return len_res, res
    else:
        return 0, '0'


def subseq(n, lst):
    if n == 0:
        storage.append(is_subseq(lst))
        return
    subseq(n - 1, lst + [True])
    subseq(n - 1, lst + [False])


subseq_in = open('subsequences.in', 'r')
subseq_out = open('subsequences.out', 'w')

n = int(subseq_in.readline())
lst = list(map(int, subseq_in.readline().split()))
subseq_in.close()

storage = []
subseq(n, [])
for i in range(len(storage) - 1):
    print(storage[i][0], storage[i][1], file=subseq_out)
subseq_out.close()
