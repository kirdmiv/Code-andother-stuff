cur_ans = ["0"]
for i in range(20):
    for i in range(len(cur_ans)):
        if cur_ans[i] == "0":
            cur_ans.append("1")
        elif cur_ans[i] == "1":
            cur_ans.append("2")
        elif cur_ans[i] == "2":
            cur_ans.append("0")
#print(*cur_ans, sep="")

ans = []
import math
#n = int(input())
for n in range(1, 1048577):
    n-=1
    cnt = 0
    while n > 0:
        n-=2 ** int(math.log2(n))
        cnt += 1
    ans.append(str(cnt%3))    
    #print(cnt%3, end='')
print(len(ans), len(cur_ans))
for i in range(len(ans)):
    if ans[i] != cur_ans[i]:
        print("cyka", i, ans[i],cur_ans[i])
print(ans==cur_ans)