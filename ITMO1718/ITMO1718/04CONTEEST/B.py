def find_max(lst):
    pos = 0
    ans = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > ans:
            ans = lst[i]
            pos = i
    return ans, pos

def find_min(lst):
    pos = 0
    ans = lst[0]
    for i in range(1, len(lst)):
        if lst[i] < ans:
            ans = lst[i]        
            pos = i
    return ans, pos


n = int(input())
lst = list(map(int, input().split()))
lst_max, pos_max = find_max(lst)
lst_min, pos_min = find_min(lst)
while lst_max != lst_min:
    lst[pos_max] -= lst_min
    lst_max, pos_max = find_max(lst)
    lst_min, pos_min = find_min(lst)
print(lst[0])