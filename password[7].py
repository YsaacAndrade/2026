<<<<<<< HEAD
import sys
import string
import re


def main():

    password = input("Insert your password: ")

    print(verify_chars(verify_length(password)))

def verify_length(password):
    if len(password) >= 16:
        return password
    else:
        sys.exit("The password must have a minimum of 16 characters.")

def find_chars(chars):
    if weak := re.search(r"[0-9][0-9][0-9]|[a-z][a-z][a-z]|[A-Z][A-Z][A-Z]", chars):
        strength = 2
        return strength

    if weak_medium := re.search(r"[0-9][0-9][0-9]|[a-z][a-z][a-z]", chars):
        strength = 4
        return strength

    if medium := re.search(r"[a-z][a-z][a-z]", chars):
        strength = 6
        return strength

    else:







def verify_chars(verified_password):
    password = verified_password
    capitalized = 0
    lower = 0
    numbers = 0
    special = 0

    for item in password:
        if item.isalpha():
            if item == item.isupper():
                capitalized += 1
            else:
                lower += 1
        elif item in string.punctuation:
            special += 1
        else:
            numbers += 1

    if capitalized <= 6 and lower <= 6 and numbers <= 6 and special <= 6:
        return "Password force: MediumC\nConsider to use more special characters"

    if capitalized >= 6 and lower >= 6 and numbers >= 6 and special >= 6:
       return "Password force: Strong"

    else:
        return "Password force: Weak\nConsider using different characters"


if __name__ == "__main__":
=======
import sys
import string

def main():

    password = input("Insert your password: ")

    print(verify_chars(verify_length(password)))

def verify_length(password):
    if len(password) >= 16:
        return password
    else:
        sys.exit("The password must have a minimum of 16 characters.")


def verify_chars(verified_password):
    password = verified_password
    capitalized = 0
    lower = 0
    numbers = 0
    special = 0

    for item in password:
        if item.isalpha():
            if item == item.isupper():
                capitalized += 1
            else:
                lower += 1
        elif item in string.punctuation:
            special += 1
        else:
            numbers += 1

    if capitalized <= 6 and lower <= 6 and numbers <= 6 and special <= 6:
        return "Password force: MediumC\nConsider to use more special characters"

    if capitalized >= 6 and lower >= 6 and numbers >= 6 and special >= 6:
       return "Password force: Strong"

    else:
        return "Password force: Weak\nConsider using different characters"


if __name__ == "__main__":
>>>>>>> 7da541f6bd82c4034928e78fa215699c606660b5
    main()