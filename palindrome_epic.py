import os
import re
import sys

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def is_palindrome(line):
    line = re.sub(r'[^A-Za-z]', '', line)
    line = line.lower()
    reversed_string = reverse_string(line)
    if line == reversed_string:
        return True
    else:
        return False


def reverse_string(line):
    if len(line) == 0:
        return ''
    return reverse_string(line[1:]) + line[0]


def main():
    clear()

    with open(sys.argv[1], 'r') as f:
        for line in f:
            if is_palindrome(line):
                print("Yep,'{}'is a palindrome!".format(line))
            else:
                print("Sorry,'{}'is not a palindrome.".format(line))

    again = input("Run again? [y/N] \n")
    if again.lower() == 'y':
        main()

    clear()


if __name__ == '__main__':
    main()
