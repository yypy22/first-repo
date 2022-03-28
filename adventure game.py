#adventure game
#mini project
import random
def ad():
    adventure = input("You started your adventure, and encountered wolves. What would you do?Attack/Escape/Wait: ")
    if adventure == "Attack": 
        attack()
    elif adventure == "Escape": 
        escape()
    elif adventure == "Wait":
        wait()
def attack():
    print("You died and were eaten. Bad choice")
def escape():
    miracle = random.randint(0,2)
    future = ["Eaten", "Won", "Again"]
    d = future[miracle]
    if d == "Eaten ":
        print("You were eaten"+char)
    elif d == "Won":
        print("You won. You are alive")
    elif d == "Again":
        again()
def wait(): 
    print("Worst choice, you dead! Pigs are not strong...")
def again():
    ad()
name = input("Who are you?: ")
print("Welcome:" + name + "!")
pigs = ["boo", "poo", "hoo"]
char = input("Which do you choose? boo/poo/hoo: ")
if char not in pigs:
    print("Pigs are not for you, good bye")
if char in pigs: 
    if char == "boo":
        a = char
        ad()
    elif char == "poo": 
        b = char
        ad()
    elif char == "hoo": 
        c = char
        ad()


    
    
    
    
    