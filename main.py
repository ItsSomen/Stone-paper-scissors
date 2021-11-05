import random

option = ["stone", "paper", "scissors"]

print("Welcome to Rock paper scissors Game")
print("By - Somen ")

comp_choice = 0
user_choice = 0

def sps():
    a = 1
    user_point = 0
    comp_point = 0
    for i in option:
        print("Choose you move")
        print(a," ",i)
        a+=1
    for running in range (0,10):
        comp_choice = random.choice(option)
        user_choice = int(input("Enter your Chioce(1/2/3): "))
        if (user_choice >= 1 and user_choice <=3):
            print("you choose ", option[user_choice])
            print("computer choose ", comp_choice)
            if comp_choice == "stone":
                if user_choice == 2:
                    print("You win this time")
                    print("Adding 1 point to user")
                    user_point += 1
                    print("Users point = ", user_point)
                    print("Computer point = ", comp_point)
                    print()
                    print()
                elif user_choice == 1:
                    print("Draw, No change in points")
                    print()
                    print()
                else:
                    print("Computer Wins")
                    print("Adding 1 point to computer")
                    comp_point += 1
                    print("Users point = ", user_point)
                    print("Computer point = ", comp_point)
                    print()
                    print()

            elif comp_choice == "paper":
                if user_choice == 3:
                    print("You win this time")
                    print("Adding 1 point to user")
                    user_point += 1
                    print("Users point = ", user_point)
                    print("Computer point = ", comp_point)
                    print()
                    print()
                elif user_choice == 2:
                    print("Draw, No change in points")
                    print()
                    print()
                else:
                    print("Computer Wins")
                    print("Adding 1 point to computer")
                    comp_point += 1
                    print("Users point = ", user_point)
                    print("Computer point = ", comp_point)
                    print()
                    print()
            
            else:
                if user_choice == 1:
                    print("You win this time")
                    print("Adding 1 point to user")
                    user_point += 1
                    print("Users point = ", user_point)
                    print("Computer point = ", comp_point)
                    print()
                    print()
                elif user_choice == 3:
                    print("Draw, No change in points")
                    print()
                    print()
                else:
                    print("Computer Wins")
                    print("Adding 1 point to computer")
                    comp_point += 1
                    print("Users point = ", user_point)
                    print("Computer point = ", comp_point)
                    print()
                    print()
        else:
            print("make a legal move please")
            print("chioce 1, 2 or 3")
        
    if user_point > comp_point:
        print("You Win from computer")
    elif user_point == comp_point:
        print("Its a draw")
    else:
        print("Computer wins from you, Better luck next time")
                    
if __name__ == "__main__":
    sps()