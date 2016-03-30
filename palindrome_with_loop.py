import os
import re

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def get_string():
    user_string = input("What do you want to check?\n")

    for value in user_string:
        if value.isdigit():
            print("You must not be from around here. We only accept letters and symbols in these parts.\n >")
            return get_string()

    return user_string


def is_palindrome(user_string):
    user_string = re.sub(r'[^A-Za-z]', '', user_string)
    user_string = user_string.lower()
    reversed_string = reverse_string_loop(user_string)
    if user_string == reversed_string:
        return True
    else:
        return False


def reverse_string(user_string):
    if len(user_string) == 0:
        return ''
    return reverse_string(user_string[1:]) + user_string[0]

def reverse_string_loop(user_string):
    reversed_list = []
    for value in user_string:
        reversed_list.insert(0, value)

    return "".join(reversed_list)

def main():
    clear()
    user_string = get_string()

    if is_palindrome(user_string):
        clear()
        print("Yep,", user_string, "is a palindrome!")
    else:
        clear()
        print("Sorry,", user_string, "is not a palindrome.")

    again = input("Run again? [y/N] \n")
    if again.lower() == 'y':
        main()

    clear()


if __name__ == '__main__':
    main()
