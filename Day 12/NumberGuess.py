from art import logo
import random

EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5

def check_answer(guess,answer,turns):
    if guess>answer:
        print("Too high!")
        return turns-1
    elif guess<answer:
        print("Too low!")
        return turns-1
    else:
        turns=0
        print(f"You got it, the answer was {answer}")

def set_difficulty():
    level=input("Choose a difficulty 'easy' or 'hard': ")
    if level=='easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100")
    answer=random.randint(1,100)
    print(f"Psst! The number is {answer}")

    turns=set_difficulty()
    guess=0
    while guess!=answer:
        print(f"You have {turns} attempts remaining to guess the number!")

        guess=int(input("Make a guess: "))

        turns=check_answer(guess,answer,turns)

        # turns-=1

        if turns==0:
            print("You ran out of attempts, you lose!")
            return
        elif guess!=answer:
            print("Guess again!")

game()