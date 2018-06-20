def check_king():
    flag = False
    for i in range(position[0] - 1, position[0] + 2):
        for j in range(position[1] - 1, position[1] + 2):
            res = [i, j]
            for k in rooks:
                if (i != k[0] and j != k[1]) or (i == k[0] and j == k[1]):
                    pass
                else:
                    res = []
                    break
            if res:
                if res[0] == position[0] and res[1] == position[1]:
                    flag = True
                else:
                    return chr(res[0] + ord('a') - 1) + str(res[1])
    if flag:
        return "Stalemate"
    return "Checkmate"


rooks_in = open('rooks.in', 'r')
rooks_out = open('rooks.out', 'w')

# Читаем
position = list(map(str, rooks_in.readline().rstrip()))
position[0] = ord(position[0]) - ord('a') + 1
position[1] = int(position[1])

n = int(rooks_in.readline())
rooks = [[0, 0], [0, 9], [9, 0], [9, 9]]

for j in range(n):
    rook_position = list(map(str, rooks_in.readline().rstrip()))
    rook_position[0] = ord(rook_position[0]) - ord('a') + 1
    rook_position[1] = int(rook_position[1])
    rooks.append(rook_position)
rooks_in.close()

print(check_king(), file=rooks_out)
rooks_out.close()
