import random
import sys

def main():

    user = input("Rock, paper or Scissors? ").strip().lower()

    print(who_win(verify_input(user), enemy_value()))

def verify_input(user_input):
    user = user_input

    if user not in ("rock", "paper", "scissors"):
        sys.exit("Please, select one between Rock, Paper and Scissors.")
    return user

def enemy_value():
    return random.choice(["rock", "paper", "scissors"])

def who_win(user, randomness):
    if user == "rock" and randomness == "paper":
        print(f"Randomness select: {randomness}!")
        return "Randomness Wins!"

    if user == "scissor" and randomness == "paper":
        print(f"Randomness select: {randomness}!")
        return "User Wins!"

    if user == "paper" and randomness == "rock":
        print(f"Randomness select: {randomness}!")
        return "User Wins!"

    if user == "rock" and randomness == "scissors":
        print(f"Randomness select: {randomness}!")
        return "User Wins!"

    if user == "scissors" and randomness == "rock":
        print(f"Randomness select: {randomness}!")
        return "Randomness Wins!"

    if user == "paper" and randomness == "scissors":
        print(f"Randomness select: {randomness}!")
        return "Randomness Wins!"

    print(f"Randomness select: {randomness}!")
    return "Draw."


if __name__ == "__main__":
    main()