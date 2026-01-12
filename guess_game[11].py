from random import randint

def main():

    print("Game: A random number between 0 - 100 will be generated, try to get it right.\n\nYou have 5 attempts.")

    print(user_input(number(0, 100)))

def user_input(number):
    attempts = 5
    print(number)

    while (attempts > 0) and (attempts <= 5):
        user = str(input("What's the number? "))


        if user.isalpha():
            attemtps -= 1
            print(f"You have {attempts} attempts")
            continue


        if user != number:
            attempts -= 1
            print(f"You have {attempts} attempts")
            continue


        if user == number:
            return "You Win!"


    return f"You lose, the number is {number}"



def number(n1, n2):
    n = randint(n1, n2)
    return str(n)



if __name__ == "__main__":
    main()