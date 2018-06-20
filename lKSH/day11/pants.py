pants_in = open('pants.in', 'r')
pants_out = open('pants.out', 'w')

n = pants_in.readline()
print(len(set(pants_in.readline().split())), file=pants_out)
pants_in.close()
pants_out.close()
