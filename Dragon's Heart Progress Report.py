import tkinter
import turtle
import time


wn = turtle.Screen()
wn.setup(width=1280, height=720, startx=None, starty=None)
wn.title("Dragon's Heart")
wn.bgpic("C:\\Users\\Andre\\Downloads\\Dragon Folder\\BGscreen1.png")


turt = turtle.Turtle()



turt.hideturtle()
turt.penup()


#wn.register_shape("SB1.gif" , shape=None)


#image = "C:\\Users\\Andre\\Downloads\\SB1.gif"

#wn.addshape("C:\\Users\\Andre\\Downloads\\SB1.gif")
#turt.shape("C:\\Users\\Andre\\Downloads\\SB1.gif")


#square
turt.goto(-250 , -280)
turt.showturtle()
turt.pendown()
turt.pencolor("Aquamarine")
turt.pensize(8.5)
turt.forward(500)
turt.left(90)
turt.forward(100)
turt.left(90)
turt.forward(500)
turt.left(90)
#start
turt.forward(100)
turt.penup()
turt.goto(-140,-260)
turt.pendown()
#turtle.write("Start", move=False, align="left", font=("Arial", 24, "normal"))
#turt.write("start")


#Letter S
turt.speed(8)


turt.left(90)
turt.forward(30)
turt.left(90)
turt.forward(30)
turt.left(90)
turt.forward(30)
turt.right(90)
turt.forward(30)
turt.right(90)
turt.forward(30)

#Letter T
turt.penup()
turt.forward(40)
turt.pendown()
turt.right(90)
turt.forward(60)
turt.backward(60)
turt.right(90)
turt.forward(20)
turt.backward(40)
turt.penup()
turt.left(90)
turt.forward(30)
turt.right(90)

#Letter A
turt.right(90)
turt.forward(30)
turt.right(90)
turt.forward(25)
turt.right(90)
turt.pendown()
turt.forward(60)
turt.backward(60)
turt.left(90)
turt.forward(40)
turt.right(90)
turt.forward(60)
turt.backward(30)
turt.right(90)
turt.forward(40)
turt.backward(40)
turt.right(90)
turt.forward(30)
turt.right(90)

#Letter R
turt.penup()
turt.forward(30)
turt.right(90)
turt.pendown()
turt.forward(60)
turt.backward(60)
turt.left(90)
turt.forward(40)
turt.right(90)
turt.forward(30)
turt.right(90)
turt.forward(40)
turt.left(145)
turt.forward(50)
turt.backward(50)
turt.left(125)
turt.forward(30)
turt.right(90)
turt.forward(40)

#Letter T Last Letter
turt.penup()
turt.forward(20)
turt.pendown()
turt.forward(40)
turt.backward(20)
turt.right(90)
turt.forward(60)

#Game Name
turt.penup()
turt.home()
turt.backward(10)
#turt.write("Dragon's Heart", fonts)
turt.pencolor("dark blue")
turt.write("Dragon's Heart", move=False, align="center", font=("Arial", 100, "normal"))
turt.hideturtle()
turt.forward(100)

Hearts = ['H1', 'H2', 'H3']
score = []


def Start_Game():
    x = input(str("Yes to start, No to quit: "))

    if x == 'Yes' or x == 'yes':
        pass
    elif x == 'No' or x == 'no':
        quit()
    else:
        Start_Game()
    
Start_Game()


turtle.resetscreen()

def BP1():
    wn.setup(width=700, height=406, startx=None, starty=None)
    wn.bgpic("C:\\Users\\Andre\\Downloads\\Dragon Folder\\BG3.png")
    
    turt.speed(0)
    turt.pencolor("white")
    turt.penup()
    turt.goto(0,70)
    turt.pendown()
    turt.write("(A Stranger Approaches You from the Dark) … Hello young traveler, I see you have come for the dragon's heart", move=False, align="center", font=("Arial", 10, "normal"))
    turt.penup()
    turt.goto(0,55)
    turt.pendown()
    turt.write("But be warned, many a hero have tried before, and yet the treasure still remains.", move=False, align="center", font=("Arial", 10, "normal"))
    turt.penup()
    turt.goto(0,40)
    turt.pendown()
    turt.write("You have a long and hard journey ahead of you", move=False, align="center", font=("Arial", 10, "normal"))
    turt.penup()
    turt.goto(0,25)
    turt.pendown()
    turt.write("Be wary, there is much more than dragons you have to worry about on your journey.", move=False, align="center", font=("Arial", 10, "normal"))
    turt.penup()
    turt.goto(0,10)
    turt.pendown()
    turt.write("Alas, I cannot come with, but I do wish you the best of luck. (Stranger walks off with an ominous grin upon his face)", move=False, align="center", font=("Arial", 10, "normal"))

   
    
def Game_Over():
    wn.setup(width=640, height=640, startx=None, starty=None)
    wn.bgpic("C:\\Users\\Andre\\Downloads\\Dragon Folder\\GameOver.png")

    print("Game Over")
    print("score: ", sum(score))


BP1()






B1 = input(str("press any key to continue:"))

