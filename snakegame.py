

from tkinter import *
import random 

Gwidth = 550
Gheight = 550

def placeFood():
   global food, foodX, foodY
   food = canvas.create_rectangle(0,0, snakeSize, snakeSize, fill="steel blue" )
   foodX = random.randint(0,Gwidth-snakeSize)
   foodY = random.randint(0,Gheight-snakeSize)
   canvas.move(food, foodX, foodY)
 
direction = "down"

def leftKey(event):
   global direction
   direction = "left"
   
   

def rightKey(event):
   global direction
   direction = "right"
   
   
def upKey(event):
   global direction
   direction = "up"
  
   
def downKey(event):
   global direction
   direction = "down"



positions = [0]

def moveSnake():
    canvas.pack()
    positions = []
    positions.append(canvas.coords(snake[0]))
    if positions[0][0] < 0:
        gameover = True
        canvas.create_text(Gwidth/2,Gheight/2,fill="white",font="Times 20 italic bold", text="Game Over!")
    elif positions [0][2] > Gwidth:
        gameover = True
        canvas.create_text(Gwidth/2,Gheight/2,fill="white",font="Times 20 italic bold", text="Game Over!")
    elif positions[0][3] > Gheight:
        gameover = True
        canvas.create_text(Gwidth/2,Gheight/2,fill="white",font="Times 20 italic bold", text="Game Over!")
    elif positions[0][1] < 0:
        gameover = True 
        canvas.create_text(Gwidth/2,Gheight/2,fill="white",font="Times 20 italic bold", text="Game Over!")
    else: 
        gameover = False

    positions.clear()
    positions.append(canvas.coords(snake[0]))

    if direction == "left":
      canvas.move(snake[0], -snakeSize,0)
    elif direction == "right":
      canvas.move(snake[0], snakeSize,0)

    elif direction == "up":
      canvas.move(snake[0], 0,-snakeSize)
    elif direction == "down":
      canvas.move(snake[0], 0,snakeSize)

    sHeadPos = canvas.coords(snake[0])
    foodPos = canvas.coords(food)
    if overlapping(sHeadPos, foodPos):
        moveFood()
        growSnake()

    for i in range(1,len(snake)):
        positions.append(canvas.coords(snake[i]))
    for i in range(len(snake)-1):
        canvas.coords(snake[i+1],positions[i][0], positions[i][1],positions[i][2],positions[i][3])

    for i in range(1,len(snake)):
        if overlapping(sHeadPos, canvas.coords(snake[i])):
            gameOver = True
            canvas.create_text(Gwidth/2,Gheight/2,fill="white",font="Times 20 italic bold", text="Game Over!")
    if 'gameOver' not in locals():
        window.after(90, moveSnake)
    
def moveFood():
    global food, foodX, foodY
    canvas.move(food, (foodX*(-1)), (foodY*(-1)))
    foodX = random.randint(0,Gwidth-snakeSize)
    foodY = random.randint(0,Gheight-snakeSize)
    canvas.move(food, foodX, foodY)

def overlapping(a,b):
    if a[0] < b[2] and a[2] > b[0] and a[1] < b[3] and a[3] > b[1]:
        return True
    
    return False

def growSnake():
    lastElement = len(snake)-1
    lastElementPos = canvas.coords(snake[lastElement])
    snake.append(canvas.create_rectangle(0,0, snakeSize,snakeSize,fill="#FDF3F3"))
    if (direction == "left"):
        canvas.coords(snake[lastElement+1],lastElementPos[0]+snakeSize,lastElementPos[1],lastElementPos[2]+snakeSize,lastElementPos[3])
    elif (direction == "right"):
        canvas.coords(snake[lastElement+1],lastElementPos[0] -snakeSize,lastElementPos[1],lastElementPos[2] -snakeSize,lastElementPos[3])

    elif (direction == "up"):
        canvas.coords(snake[lastElement+1],lastElementPos[0],lastElementPos[1]+snakeSize,lastElementPos[2],lastElementPos[3]+snakeSize)
    else:
        canvas.coords(snake[lastElement+1],lastElementPos[0],lastElementPos[1]-snakeSize,lastElementPos[2],lastElementPos[3]-snakeSize)

    global score
    score += 10
    txt = "Score:" + str(score)
    canvas.itemconfigure(scoreText, text=txt)



window = Tk()
canvas = Canvas(window, bg="black", width=Gwidth, height=Gheight)
canvas.pack()
canvas.bind("<Left>", leftKey)
canvas.bind("<Right>", rightKey)
canvas.bind("<Up>", upKey)
canvas.bind("<Down>", downKey)
canvas.focus_set()
snake = []
snakeSize = 15
snake.append(canvas.create_rectangle(snakeSize,snakeSize, snakeSize *2, snakeSize * 2, fill="white" ))
score = 0
txt = "Score:" + str(score)
scoreText = canvas.create_text( Gwidth/2 , 10 , fill="white" ,font="Times 15 italic bold", text=txt)
window.title("Snake Game")
window.update()
screen_width = window.winfo_screenwidth() # computers screen size
screen_height = window.winfo_screenheight()       
window_width = window.winfo_width()
window_height = window.winfo_height()
x = (screen_width/2) - (window_width/2) # calculate center
y = (screen_height/2) - (window_height/2)
window.geometry('%dx%d+%d+%d' % (window_width, window_height, x, y)) # window size

placeFood()
moveSnake()


window.mainloop()
