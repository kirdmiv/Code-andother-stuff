fout = open("cards.in", 'w')
ans=[]
ans1=[]
ans2=[]
ans3=[]
ans4=[]
ans5=[]

for i1 in range(2):
    ans = []
    if i1 == 1:
        ans.append('R')
    else:
        ans.append('B')
    for i2 in range(2):
        ans1 = ans
        if i2 == 1:
            ans1.append('R')
        else:
            ans1.append('B')
        for i3 in range(2):
            ans2 = ans1
            if i3 == 1:
                ans2.append('R')
            else:
                ans2.append('B')
            for i4 in range(2):
                ans3 = ans2
                if i4 == 1:
                    ans3.append('R')
                else:
                    ans3.append('B')
                for i5 in range(2):
                    ans4 = ans3
                    print(ans3, ans4)
                    if i5 == 1:
                        ans4.append('R')
                    else:
                        ans4.append('B')
                    print(5, file=fout)
                    print(*ans4[-5:], sep='', file=fout)

fout.close()