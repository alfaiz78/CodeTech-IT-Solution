import random
ans_yes =['YES','Y','Yes','yer','y']
ans_no = ['NO','N','No','n','no']

ans = input(""" If you want to generate a random password '10 length combinations' press 'yes' 
                and you can change a length password combinations press 'no'
                >>
""")

if ans in ans_no:
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    string_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                         'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                         'z']

    string_p = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                         'I', 'J', 'K', 'l', 'M', 'N', 'O', 'P', 'Q',
                         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                         'Z']

    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
               '*', '(', ')', '<']

    all_characters = string_letters + DIGITS + string_p + SYMBOLS


    length = int(input("Enter the length of the password: "))


    password = ''.join(random.choices(all_characters, k=length))
    print("")


    print("Your password is:", password)
else:
    if ans in ans_yes:
        DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        string_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                          'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                          'z']

        string_p = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                    'I', 'J', 'K', 'l', 'M', 'N', 'O', 'P', 'Q',
                    'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                    'Z']

        SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
                   '*', '(', ')', '<']

        all_characters = string_letters + DIGITS + string_p + SYMBOLS

        length = 10

        password = ''.join(random.choices(all_characters, k=length))
        print("")

        print("Your password is:", password)
    else:
        print("you type in wroung keyword")
