import sys
from random import randint

#Guess with computer hints
def random_select_easy(x):
    random_number = randint(1,x)
    guess = 0
    while guess != random_number:
        try:
            guess = int(input(f"Guess a number between 1 and {x}: "))
            if guess < random_number:
                print("Sorry, guess too low.")
            elif guess > random_number:
                print("Sorry, guess to high.")

        except ValueError:
            print("Please enter a number")

    print(f"Yay, Congrats, you have guessed the right number {random_number} correctly!!!")

# Guess without computer hints
def random_select_not_easy(x):
    random_number = randint(1,x)
    guess = 0
    while guess != random_number:
        try:
            guess = int(input(f"Guess number (from 1 - {x}): "))
            if guess != random_number:
                print("Please, input number from 1 - 10")
                
        except ValueError:
            print("Please enter a number")
            continue
    
    print(f"Yay, Congrats, you have guessed the right number {random_number} correctly!!!")

# Computer guessing your number
def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "C":
        try:
            if low != high:
                guess = randint(low, high)
            else:
                guess = low #could be high because high == low
                break
            feedback = input(f"is {guess} too high (H), too low (L), or correct(C): ").upper()
            if feedback == "H":
                high = guess - 1
            elif feedback == "L":
                low = guess + 1
        except ValueError:
            print("Please enter a number")
            

    print(f"Yay, the computer guessed your number {guess} correctly!!")


if __name__ == "__main__":
    print("Welcome.")
    print("easy: The computer gives hints regarding your guesses")
    print("not easy: The computer does not give hints regarding your guesses")
    print("Computer: Get the computer to guess your numbers")

    difficulty = input("Choose; A = easy, B = not easy, C = computer : ").upper()

    if difficulty == "A":
        number = int(input("input range you wish to guess, 1 to __: "))
        random_select_easy(number)
    elif difficulty == "B":
        number = int(input("input range you wish to guess, 1 to __: "))
        random_select_not_easy(number)
    elif difficulty == "C":
        number = int(input("input range you wish computer to guess, 1 to __: "))
        computer_guess(number)