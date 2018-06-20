name = list(input())
letters = list(input().split())
nums = list(map(int, input().split()))
fav_letter = input()
for i in range(len(letters)):
    for j in range(len(name)):
        if letters[i] == name[j]:
            if len(nums) != 0:
                for k in nums:
                    if j == k:
                        break
                else:
                    name[j] = fav_letter
            else:
                name[j] = fav_letter
ans = ''
for i in name:
    ans += i
print(ans)
