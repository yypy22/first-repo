
#mini projects 
#simple Quiz Game 3/26 2022
def quit():
    print("Well, next time lets play together!")
    
def game():
    answer = input("What is the most well known company starting from spell a?")
    if(answer == "apple"):
        print("Great, well done!")
    else:
        print("No, try again or quit")
        gameAgain()
def gameAgain():
    rep = input("Would you like to play again or not? put Yes or Quit")
    if rep == "Yes":
        game()
    elif rep == "Quit":
        quit()

        
print("Welcome to my game quiz")
Play = input("Do you want to play?: ")
print(Play)
if Play == "Yes" or Play == "y" or Play == "Y" or Play == "yes":
    game()
else:
    quit()


    







































	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	