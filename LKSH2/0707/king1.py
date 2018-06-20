def king():
    if n % 2 == 1 and m % 2 == 1:
        return 2
    return 1


king_in = open('king1.in', 'r')
king_out = open('king1.out', 'w')

# Читаем
m, n = map(int, king_in.readline().split())
king_in.close()

print(king(), file=king_out)
king_out.close()
