def main():

    user = input("Expression: ")

    def clean(user_input):
        x = user_input.split()
        if x[0].isalpha() or x[2].isalpha():
            raise ValueError("Please, insert only number before and after the operator signal. ")
        else:
            if x[1] not in ("+", "-", "/", "x", "**"):
                raise ValueError("Please, insert correct operator.")
        return user_input

    def calculator(clean_input):
        if "+" in clean_input:
            clean_input = clean_input.split("+")
            return int(clean_input[0]) + int(clean_input[1])

        if "-" in clean_input:
            clean_input = clean_input.split("-")
            return int(clean_input[0]) - int(clean_input[1])

        if "x" in clean_input:
            clean_input = clean_input.split("x")
            return int(clean_input[0]) * int(clean_input[1])

        if "/" in clean_input:
            clean_input = clean_input.split("/")
            return int(clean_input[0]) / int(clean_input[1])

        if "**" in clean_input:
            clean_input = clean_input.split("**")
            return int(clean_input[0]) ** int(clean_input[1])

        return ValueError
    print(calculator(clean(user)))

if __name__ == "__main__":
    main()