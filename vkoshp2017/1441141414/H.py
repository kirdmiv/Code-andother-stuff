fin = open("secure.in", "r")
fout = open("secure.out", "w")

n, m = map(int, fin.readline().split())
a = list(map(int, fin.readline().split()))
g = [[]] * n
for i in range(m):
    s, t, c = map(int, fin.readline().split())
    