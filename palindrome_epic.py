import os
import re

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def get_file():
    string_file = input("What do you want to check?\n")

    for value in string_file:
        if value.isdigit():
            print("You must not be from around here. We only accept letters and symbols in these parts.\n >")
            return get_string()

    return string_file


def is_palindrome(string_file):
    string_file = re.sub(r'[^A-Za-z]', '', string_file)
    string_file = string_file.lower()
    reversed_string = reverse_string(string_file)
    if string_file == reversed_string:
        return True
    else:
        return False


def reverse_string(string_file):
    if len(string_file) == 0:
        return ''
    return reverse_string(string_file[1:]) + string_file[0]


def main():
    clear()
    string_file = get_string()

    if is_palindrome(string_file):
        clear()
        print("Yep,'{}'is a palindrome!".format(string_file))
    else:
        clear()
        print("Sorry,'{}'is not a palindrome.".format(string_file))

    again = input("Run again? [y/N] \n")
    if again.lower() == 'y':
        main()

    clear()


if __name__ == '__main__':
    main()
