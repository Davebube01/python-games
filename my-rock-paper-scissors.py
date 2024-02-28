import random

class dey_play():
    def __init__(self, user, computer) -> None:
        self.user = user
        self.computer = computer


    def play(self):
        print(f"user picked {self.user}")
        print(f"computer picked {self.computer}")

        if self.user == self.computer:
            print("It's a tie")
        
        elif self.is_win(self.user, self.computer):
            print("You Won!")
        
        else:
            print("You Lost!")
        
        
    def is_win(self, user, computer):
        # r > s, s > p, p > r

        if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
            return True
        

def play_game():
    user = input("Whats your choice? 'r' for rock, 'p' for paper, 's' for scissors:\n").lower()
    # if user == 'r' or user == 'p' or user == 's':
    computer = random.choice(['r', 'p', 's'])
    p = dey_play(user, computer)
    p.play()
    # else:
    # print("please, input a number")

if __name__ == "__main__":
    play_game()