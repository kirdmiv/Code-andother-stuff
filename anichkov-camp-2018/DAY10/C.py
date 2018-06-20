def lexical(prev_string, open_brackets, close_brackets):
    if open_brackets == close_brackets == 0:
        print(prev_string, file=lexical_out)
    if open_brackets != 0 and open_brackets <= close_brackets:
        lexical(prev_string + "(", open_brackets - 1, close_brackets)
    if close_brackets != 0 and close_brackets >= open_brackets:
        lexical(prev_string + ")", open_brackets, close_brackets - 1)

lexical_in = open('brackets.in', 'r')
lexical_out = open('brackets.out', 'w')

# Читаем
n = int(lexical_in.readline())
lexical_in.close()

lexical("", n, n)
lexical_out.close()