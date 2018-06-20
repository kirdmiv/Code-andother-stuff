len_lst = int(input())
lst = list(map(int, input().split()))
num, place = map(int, input().split())
lst = lst[:place - 1] + [num] + lst[place - 1:]
print(*lst)
