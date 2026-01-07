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
    main()