import random

class dey_play():
    def __init__(self, user, computer) -> None:
        self.user = user
        self.computer = computer


    def play(self):
        user_score = 0
        comp_score = 0
        
        # statements
        if user_score < 3 or comp_score < 3:
            print(f"user picked {self.user} and computer picked {self.computer}")
            if self.user == self.computer:
                    print("It's a tie")
                
            elif self.is_win(self.user, self.computer):
                print("You Won!")
                user_score += 1
            
            else:
                print("You Lost!")
                comp_score += 1

            print(f"user {user_score} : {comp_score} Computer")

            # while loop
            while user_score < 3 and comp_score < 3:
                self.user = input("Whats your choice? 'r' for rock, 'p' for paper, 's' for scissors:\n").lower()
                if self.user == "r" or self.user == "p" or self.user == "s":
                    self.computer = random.choice(['r', 'p', 's'])
                    print(f"user picked {self.user} and computer picked {self.computer}")
                    if self.user == self.computer:
                        print("It's a tie")
                    
                    elif self.is_win(self.user, self.computer):
                        print("You Won!")
                        user_score += 1
                    
                    else:
                        print("You Lost!")
                        comp_score += 1

                    print(f"user {user_score} : {comp_score} Computer")
                
                else:
                    print("please input either r,p or s")

        # results after game has been played
        if user_score > comp_score:
            print("YAY!! You have won")
            print(f"user {user_score} : {comp_score} Computer")
        elif comp_score > user_score:
            print("sorry! You've lost")
            print(f"user {user_score} : {comp_score} Computer")
        
        
    def is_win(self, user, computer):
        # r > s, s > p, p > r
        if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
            return True
        

def play_game():
    user = input("Whats your choice? 'r' for rock, 'p' for paper, 's' for scissors:\n").lower()
    if user == "r" or user == "p" or user == "s":
        computer = random.choice(['r', 'p', 's'])
        p = dey_play(user, computer)
        p.play()
    else:
        print("please input either r,p or s")
        user = input("Whats your choice? 'r' for rock, 'p' for paper, 's' for scissors:\n").lower()
        computer = random.choice(['r', 'p', 's'])
        p = dey_play(user, computer)
        p.play()

if __name__ == "__main__":
    play_game()