#rock paper scissors
#mini project
import random 
user = 0
computer = 0
options = ["Rock", "Scissors", "Paper"]
while True: 
    user = input("Rock?Scissors?Paper?Quit?: ")
    if user == "Quit":
        break
    if user not in options:
        break
    else:
        random_num = random.randint(0, 2)
        computer = options[random_num]
        if user == "Rock" and computer == "Rock":
            print("Draw!")
            break
        if user == "Rock" and computer == "Scissors":
            print("Won")
            break
        if user == "Rock" and computer == "Paper":
            print("Lost")
            break
        if user == "Scissors" and computer == "Rock":
            print("Lost")
            break
        if user == "Scissors" and computer == "Scissors":
            print("Draw")
            break
        if user == "Scissors" and computer == "Paper":
            print("Won")
            break
        if user == "Paper" and computer == "Paper": 
            print("draw")
            break
        if user == "Paper" and computer == "Rock":
            print("Won")
            break
        if user == "Paper" and computer == "Scissors":
            print("Lost")
            break 
print("See you")
        
        
