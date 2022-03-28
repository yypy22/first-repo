#mini project 
# number guess game

import random
top_number = input("What do you like the number in 1 to 1000? ")
num = random.randrange(1, 1001)
top_number = int(top_number)
if 0 < top_number and top_number <=1000: 
    while True:
        if top_number < num: 
            print("Type larger number!")
            top_number = int(input())
        elif top_number > num: 
            print("Type smaller number!")
            top_number = int(input())
        elif top_number == num: 
            print("Awesome, you guessed correctly!")
            break
else: 
    print("Type NUMBER CORRECTLY!!!")




















































