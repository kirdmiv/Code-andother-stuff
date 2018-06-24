n = int(input())
s = input()

m = [0, 0, 0, 0]

for i in range(n):
    if s[i] == "N":
        m[0] += 1
    if s[i] == "S":
        m[1] += 1    
    if s[i] == "W":
        m[2] += 1    
    if s[i] == "E":
        m[3] += 1
print(n - max(m))