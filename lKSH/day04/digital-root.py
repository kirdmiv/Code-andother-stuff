def digital_root(number):
    start_num = number
    while number >= 10:
        number = sum([int(i) for i in str(number)])
    return number, start_num


digital_root_in = open('dig-root.in', 'r')
digital_root_out = open('dig-root.out', 'w')

lst = list(map(int, digital_root_in.readline().split()))
digital_root_in.close()

lst.sort(key=digital_root)
ans = [str(i) for i in lst]
ans = ' '.join(ans)
digital_root_out.write(ans)
digital_root_out.close()
