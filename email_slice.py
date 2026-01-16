from validator_collection import validators, errors
import sys

def main():

    user = input("Email: ")

    print(slice_email(clean(user)))

def clean(mail):
    try:
        validators.email(mail)
        return mail

    except errors.EmptyValueError, errors.InvalidEmailError:
        sys.exit("Invalid email.")

def slice_email(valid_mail):
    vm = valid_mail
    vm = vm.split("@")

    name = vm[0]
    domain = vm[1]


    return f"Your username is {name} & domain is {domain}"



if __name__ == "__main__":
    main()