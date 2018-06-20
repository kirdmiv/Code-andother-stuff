import random

alphabet = ["abcdefghijklmnoprstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "123456789", "_@#*()-+|"]
length = 16
password = ""

passwords_file_out = open("passwords.txt", 'w')
passwords_file_in  = open("passwords.txt", 'r')

while True:
    key = list(input().split())
    print(key)

    if key[0] == "exit":
        break

    if key[0] == "new":
        for i in range(length):
            rand = random.randint(1, len(alphabet)) - 1
            password += alphabet[rand][random.randint(0, len(alphabet[rand]) - 1)]
        print(key[1], key[2], password, file=passwords_file_out)
    elif key[0] == "get":
        passwords = []
        get_password = list(input().split())
        while get_password != 0:
            passwords.append(get_password[0])
            passwords.append(get_password[1])
        index = passwords.find(key[2])
        print(key[1], passwords[index + 1])

passwords_file_out.close()
passwords_file_in.close()