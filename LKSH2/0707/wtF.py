res = []
lol = open("lol.in", "r")
for i in range(25):
    res.append(lol.readline().rstrip())
res.reverse()
for i in range(len(res)):
    print(res[i])