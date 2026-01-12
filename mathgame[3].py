from random import randint

def main():

    diff = input("What's the difficulty? ()easy ()medium ()hard ") # 1


    def clean_input(user_input): # 2
        user = user_input.lower().strip()
        if user not in ("easy", "medium", "hard"):
            raise ValueError("Select an valid Difficulty!")
        else:
            return user


    def pre_game(difficulty):
        if difficulty == "easy":
            return easy(10)

        if difficulty == "medium":
            return medium(10)

        if difficulty == "hard":
            return hard(10)

        else:
            raise ValueError("Error! :(")


### IF USER SELECT EASY ###
    def easy(num): # 3
        calcs = []
        for _ in range(num):
            number_1 = randint(1, 10)
            number_2 = randint(1, 10)
            calcs.append(f"{number_1} {number_2}")
        return calcs


### IF USER SELECT MEDIUM ###
    def medium(num): # 3
        calcs = []
        for _ in range(num):
            number_1 = randint(10, 100)
            number_2 = randint(10, 100)
            calcs.append(f"{number_1} {number_2}")
        return calcs


### IF USER SELECT HARD ###
    def hard(num): # 3
        calcs = []
        for _ in range(num):
            number_1 = randint(100, 1000)
            number_2 = randint(100, 1000)
            calcs.append(f"{number_1} {number_2}")
        return calcs

### GAME RUNNING CODE ###

    ### CONFIGS ###
    x = pre_game(clean_input(diff))
    errors = 3
    runs = 0

    for item in x:
        item = item.split()
        response = (input(f"{item[0]} + {item[1]} = "))

        if response.isalpha():
            print("Please, use only numbers!")
            break

        else:
            response = int(response)

            if response == (int(item[0]) + int(item[1])):
                runs += 1
                pass

            else:
                print(f"You have more {errors} attempts")
                errors -= 1
                runs += 1

                if errors == -1: # IN CASE OF LOSING THE GAME
                    print("You lose!")
                    break

            if runs == 10: # IN CASE OF WINNING
                print("You win!")

if __name__ == "__main__":
    main()
