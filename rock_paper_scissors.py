import random


def play():
    user = input("Whats your choice? 'r' for rock, 'p' for paper, 's' for scissors:\n").lower()
    computer = random.choice(['r', 'p', 's'])

    print(f"user picked {user}")
    print(f"computer picked {computer}")

    if user == computer:
        print("It's a tie")
    
    if is_win(user, computer):
        print("You Won!")
    
    print("You Lost!")
    
    
def is_win(user, computer):
    # r > s, s > p, p > r

    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return True
        
play()