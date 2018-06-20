def insert_sort(lst):
    for i in range(1, len(lst)):
        j = 0
        while j <= i and lst[j] > lst[i]:
            j += 1
        lst = lst[:j] + [lst[i]] + lst[j:i] + lst[i + 1:]
    return lst


sortin = open('sort.in', 'r')
sortout = open('sort.out', 'w')

n = sortin.readline()
nums = list(map(int, sortin.readline().split()))
sortin.close()

res = insert_sort(nums)
ans = [str(i) for i in res]
ans = ' '.join(ans)
sortout.write(ans)
sortout.close()
