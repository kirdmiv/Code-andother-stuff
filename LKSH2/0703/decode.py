def decode():
    lst = ['']
    for i in string:
        if lst[-1] == i:
            lst.pop()
        else:
            lst.append(i)
    return lst


decode_in = open('decode.in', 'r')
decode_out = open('decode.out', 'w')

# Читаем
string = decode_in.readline().rstrip()
decode_in.close()

print(*decode(), file=decode_out, sep='')
decode_out.close()
