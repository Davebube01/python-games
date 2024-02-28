import random
from words import wordds
import string

def get_valid_words(words):
    random_words = random.choice(words)
    # while "-" or " " in random_words:
    while '-' in words or ' ' in words:
        random_words = random.choice(words)

    return random_words.upper()

def Hangman():
    guess_words = get_valid_words(wordds)
    word_letters = set(guess_words) #Letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #What the user has guessed

    while len(word_letters) > 0:
        # Letters used
        print("You have used these letters, ", ' '.join(used_letters))

        # Current word (eg W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in guess_words]
        print("current letters: ", ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                
        elif user_letter in used_letters:
            print("You have already used that character. please try again")

        else:
            print("Invalid Character")



if __name__ == "__main__":
    Hangman()
