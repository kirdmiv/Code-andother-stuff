def printlist(s, bef, bet, aft):
    print(bef, end='')
    print(*s, sep=bet, end='')
    print(aft)


s = input().split()
printlist(s, 'x=', '*', '.')
printlist(s, '', ' ', '')
printlist(s, '', '', '')
printlist(s, '"', '","', '"')
