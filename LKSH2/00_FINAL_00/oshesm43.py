def oshesm43(prev_string, open_brackets, close_brackets):
    if open_brackets == close_brackets == 0:
        print(prev_string, file=oshesm43_out)
    if open_brackets != 0 and open_brackets <= close_brackets:
        oshesm43(prev_string + "(", open_brackets - 1, close_brackets)
    if close_brackets != 0 and close_brackets >= open_brackets:
        oshesm43(prev_string + ")", open_brackets, close_brackets - 1)

oshesm43_in = open('oshesm43.in', 'r')
oshesm43_out = open('oshesm43.out', 'w')

# Читаем
n = int(oshesm43_in.readline())
oshesm43_in.close()

oshesm43("", n, n)
oshesm43_out.close()
