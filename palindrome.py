import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def get_string():
    user_string = input("What do you want to check?\n")

    for value in user_string:
        if value.isdigit():
            print("You must not be from around here. We only accept letter and symbols in these parts.\n")
            return get_string()

    return user_string.lower()


def is_palindrome(user_string):
    reversed_string = reverse_string(user_string)
    user_string = remove_symbols(user_string)
    print("String minus symbols: ", user_string)
    print("Reversed string: ", reversed_string)
    if user_string == reversed_string:
        return True
    else:
        return False


def reverse_string(user_string):
    if len(user_string) == 0:
        return ''
    if user_string[0].isalpha():
        return reverse_string(user_string[1:]) + user_string[0]
    else:
        return reverse_string(user_string[1:])


def remove_symbols(user_string):
    regex = re.compile('[^a-z]')

    # if len(user_string) == 0:
    #     return ''
    # if user_string[0].isalpha():
    #     return user_string[0] + user_string[1:]
    # else:
    #     print("Gets to else in removal.")
    #     return user_string[1:]


def main():
    user_string = get_string()

    if is_palindrome(user_string):
        print("Yep,", user_string, "is a palindrome!")
    else:
        print("Sorry,", user_string, "is not a palindrome.")

    again = input("Run again? [y/N] \n")
    if again.lower() == 'y':
        main()

    clear()

main()
