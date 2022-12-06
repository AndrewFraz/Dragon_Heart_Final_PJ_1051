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

# End of Beginning

turtle.resetscreen()

def BP2():
    wn.setup(width=600, height=396, startx=None, starty=None)
    wn.bgpic("C:\\Users\\Andre\\Downloads\\Dragon Folder\\BG4.png")

    turt.speed(0)
    turt.pencolor("white")
    turt.penup()
    turt.goto(0,120)
    turt.pendown()
    turt.write("While Traveling, you come across a town scattered atop the mountains. ", move=False, align="center", font=("Arial", 12, "normal"))
    turt.penup()
    turt.goto(0,90)
    turt.pendown()
    turt.write(" While passing through, you find a bridge with someone blocking your way.", move=False, align="center", font=("Arial", 12, "normal"))
    turt.penup()
    turt.goto(0,60)
    turt.pendown()
    turt.write("He says he will only let you pass if you answer his riddle correctly. You accept.", move=False, align="center", font=("Arial", 12, "normal"))
    turt.penup()
    turt.goto(0,30)
    turt.pendown()
    turt.write("Voiceless it cries, Wingless but flutters, Toothless bites, Mouthless mutters", move=False, align="center", font=("Arial", 12, "normal"))

    riddle = input(str("What am I? "))

    if riddle == 'wind' or riddle == 'Wind' or riddle == 'WIND':
        print("You are a clever one, you may pass")
        score.append(5000)
        
    else:
        print("I guess you are not as clever as I thought, says the bridge keeper")
        print("To get through you now have to pay the toll. - 1 Heart.")
        del Hearts[0]
        
    

    
BP2()




turtle.resetscreen()

def BP3():
    wn.setup(width=600, height=338, startx=None, starty=None)
    wn.bgpic("C:\\Users\\Andre\\Downloads\\Dragon Folder\\BG5.png")

    turt.speed(0)
    turt.pencolor("white")
    turt.penup()
    turt.goto(0,120)
    turt.pendown()
    turt.write("While on your journey, you encounter a house. The locals of the nearby town ", move=False, align="center", font=("Arial", 12, "normal"))
    turt.penup()
    turt.goto(0,80)
    turt.pendown()
    turt.write("Tell you that it is haunted by the ghosts of the people who died there", move=False, align="center", font=("Arial", 12, "normal"))
    turt.penup()
    turt.goto(0,40)
    turt.pendown()
    turt.write("You decide to investigate and while walking down a hall you hear a voice", move=False, align="center", font=("Arial", 12, "normal"))
    turt.penup()
    turt.goto(0,0)
    turt.pendown()
    turt.write("You turn to see a ghost of a child telling you to follow her. Do you Dare follow her?", move=False, align="center", font=("Arial", 12, "normal"))

    ghost = input(str("Choose A to follow and B to run"))

    if ghost == "A" or ghost == "a":
        print("While running, you notice the ghost child following.")
        print("Come back, I'm here to help you")
        print("you escape from the house unharmed, but freighted, by what you had seen")
        score.append(100)
        

    elif ghost == "B" or ghost == "b":
        print("You follow the child down the hall. She leads you outside where she and her entire family were killed")
        print("there was gold and jewels left behind, ripe for the taking. Plus 1000 Points")
        score.append(1000)
        
        

BP3()


turtle.resetscreen()

def BP6():
    wn.setup(width=640, height=400, startx=None, starty=None)
    wn.bgpic("C:\\Users\\Andre\\Downloads\\Dragon Folder\\BG8.gif")

    turt.speed(0)
    turt.pencolor("white")
    turt.penup()
    turt.goto(0,120)
    turt.pendown()
    turt.write("while walking on a snowy path, you come across a man laying in the snow", move=False, align="center", font=("Arial", 12, "normal"))
    turt.penup()
    turt.goto(0,80)
    turt.pendown()
    turt.write("He looks pale and in need of help, he gestures toward you pleaing for help", move=False, align="center", font=("Arial", 12, "normal"))
    turt.penup()
    turt.goto(0,40)
    turt.pendown()
    turt.write("what will you do?", move=False, align="center", font=("Arial", 12, "normal"))

    charity = input(str("A to Help, B to Ignore"))

    if charity == "A" or charity == "a":
        print("You graciously help the man to his feet and walk him toward his home in the woods")
        print("You can see his home in the distance when you feel a sharp pain toward your rightside")
        print("You notice the once whitely colored snow is now a harsh red. You have been stabbed.")
        print("You try to dress the wound while the man you graciously helped starts to rob you")
        print("-300 points/-1 Heart")
        del Hearts[0]
    elif charity == "B" or charity == "b":
        print("You continue on your way avoiding the man in the path")
        print("You hear something behind you. Something is getting closer. You turn around and it is the man in the street running toward you with a knife")
        print("With your quick reflexs, you are able to disarm the man before he gets to you. Not everyone is as good as they seem.")
        print("500 points")
        score.append(500)


    

BP6()


turtle.resetscreen()


def BP7():
    wn.setup(width=1920, height=1080, startx=None, starty=None)
    wn.bgpic("C:\\Users\\Andre\\Downloads\\Dragon Folder\\DragB.gif")

    B9 = True

    turtle.register_shape("C:\\Users\\Andre\\Downloads\\Dragon Folder\\attack_1.gif")
    turtle.register_shape("C:\\Users\\Andre\Downloads\\Dragon Folder\\attack_2.gif")

    player = turtle.Turtle()
    player.shape("C:\\Users\\Andre\\Downloads\\Dragon Folder\\attack_1.gif")
    player.shapesize(50)
    player.color("green")
    player.frame = 0

    def player_animate():
            if player.frame == 0:
                    player.shape("C:\\Users\\Andre\\Downloads\\Dragon Folder\\attack_1.gif")
                    player.frame = 1
            elif player.frame == 1:
                    player.shape("C:\\Users\\Andre\\Downloads\\Dragon Folder\\attack_2.gif")
                    player.frame = 0
    
	
            # Set timer
            wn.ontimer(player_animate, 500)
            

    player_animate()
    
    turt.penup()
    turt.pencolor("white")
    turt.goto(0,-150)
    turt.pendown()
    turt.write("You are almost to the end of your journey. You can see a cave full of riches beyond your wildest dreams", move=False, align="center", font=("Arial", 25, "normal"))
    turt.penup()
    turt.goto(0,-200)
    turt.pendown()
    turt.write("The air starts to feel heavy with the scent of fire, you look up into the sky and see a Fire breathing dragon", move=False, align="center", font=("Arial", 25, "normal"))
    turt.penup()
    turt.goto(0,-250)
    turt.pendown()
    turt.write("you draw your sword and shield when you see a cave that could be used for shelter, which do you choose?", move=False, align="center", font=("Arial", 25, "normal"))

    Drag1 = input(str("choose A for cave and B for fight"))

    if Drag1 == 'A'or Drag1 == 'a':
        print("You hide in the cave when you notice bones scattered about, you soon realize that cave was the dragons feeding Grounds, the dragon launches a fireball straight at you, you lose 1 heart")
        del Hearts[0]
        if len(Hearts) == 0:
            Game_Over()
        else:
            print("You manage to escape, but barely.")
            print("With Sword in hand, you rush toward the forest when you find a piece of wood that you believe you could use to defend yourself")
            wood = input(str("choose A to pick it up and B to leave it behind"))

            if wood == 'A'or wood == 'a':
                print("you see a shadow in the corner of your eye and almost in a flash you see a large branch coming toward you")
                print("With your quick reflexes, you manage to use the wooden branch to save you from injury, pretty lucky indeed")
                print("With all the commotion, another dragon appears from the southwest and brawls against the dragon.")
                print("you use this opportunity to sneak into the dragons cave. You see the Dragons Heart Jewel right in front of you when you notice the vast treasure surrounding it")
                print("Do you choose the Dragon's Heart or The Treasure Surrounding it, Choose Carefully.")
                DC = input(str("Choose A for the Dragons Heart or B for the Treasure Surrounding it?"))
                if DC == 'A' or DC == 'a':
                    print("You take the dragons heart from its chamber, but not before the dragon returns.")
                    print("You realize you are trapped with nowhere to hide ... but wait, wait, what is that underneath the dragons heart, Its a sword inbedded in stone.")
                    print("You would recognise that sword anywhere, its Excalibur, the sword from the legends told throughout the ages. You lunge for it while the dragon breathes its ferocious firey breathe at you.")
                    print("You grab the sword and yank with all your might, the dragon rushes you from behind and with one fowl swoop you lop its head, clean off of its shoulders. You have slain the mighty dragon.")
                    print("You fall to your knees in relief. You take the dragons heart, excalibur, and as much gold as you can hold. You even take one of the dragons scales as proof of what you have done.")
                    print("Tales will be told and songs will be sung throughout the ages of your quest, to claim the Dragon Heart. End")
                    
                elif DC == 'B'or DC == 'b':
                    print("You run to the treasure surrounding the jewel and jump in, is this Heaven? gold as far as the eye can see, it seems like a paradise until you feel a warm breeze down your neck")
                    print("You ignore it and go about your business. It starts to get warmer, you wondering what is happening, am I sick?, you wonder until you look at the enterance of the cave. All you see is an eyeball starring directly at you")
                    print("You realize its the dragon. You look around, but there is nowhere to escape. You know this is the end. You cling to the gold one last time as the dragon rips off your legs and arms, and finally eats you whole. End")
                    Game_Over()
            
                
            elif wood == 'B'or wood == 'b':
                print("You hear wind whirling around you, faster and faster and faster it goes")
                print("You then notice the trees around you start to fall over and that is when you realize the dragon flying right above you")
                print("But thats not all, with the dragons wings causing a maelstrom of chaos, you see 3 fully grown trees ripped from the ground coming straight for you.")
                print("-3 hearts")
                Game_Over()
                
    elif Drag1 == 'B':
        print("You march toward the dragon to fight when you come upon a group of dead adventurers. You find some fresh food and water to help hold you over for a while. Plus 79878 points")
        print("While walking toward your foe, you notice a white scale on the ground. Do you proceed or do you wait?")
        patience = input(str("choose A to wait or B to proceed? "))
        
        if patience == 'A' or patience == 'a':
            print("you have been waiting for hours, you start to become impatient when you hear a roar from the southwest. Another dragon appears and starts battling the other dragon.")
            print("you use this opportunity to sneak into the dragons cave. You see the Dragons Heart Jewel right in front of you when you notice the vast treasure surrounding it")
            print("Do you choose the Dragon's Heart or The Treasure Surrounding it, Choose Carefully.")
            DC2 = input(str("Choose A for the Dragons Heart or B for the Treasure Surrounding it?"))
            
            if DC2 == 'A' or DC2 == 'a':
                print("You take the dragons heart from its chamber, but not before the dragon returns.")
                print("You realize you are trapped with nowhere to hide ... but wait, wait, what is that underneath the dragons heart, Its a sword inbedded in stone.")
                print("You would recognise that sword anywhere, its Excalibur, the sword from the legends told throughout the ages. You lunge for it while the dragon breathes its ferocious firey breathe at you.")
                print("You grab the sword and yank with all your might, the dragon rushes you from behind and with one fowl swoop you lop its head, clean off of its shoulders. You have slain the mighty dragon.")
                print("You fall to your knees in relief. You take the dragons heart, excalibur, and as much gold as you can hold. You even take one of the dragons scales as proof of what you have done.")
                print("Tales will be told and songs will be sung throughout the ages of your quest, to claim the Dragon Heart. End")
                
                
            elif DC2 == 'B' or DC2 == 'b':
                print("You run to the treasure surrounding the jewel and jump in, is this Heaven? gold as far as the eye can see, it seems like a paradise until you feel a warm breeze down your neck")
                print("You ignore it and go about your business. It starts to get warmer, you wondering what is happening, am I sick?, you wonder until you look at the enterance of the cave. All you see is an eyeball starring directly at you")
                print("You realize its the dragon. You look around, but there is nowhere to escape. You know this is the end. You cling to the gold one last time as the dragon rips off your legs and arms, and finally eats you whole. End")
                Game_Over()
                
        elif patience == 'B' or patience == 'b':
            print("You rush toward your opponent when you hear a rumbling sound toward the southwest.")
            print("Boom , Boom, Boom. The sound gets louder and louder until you see, oh my god, its another dragon and you are pincered between 2 fire breathing dragons.")
            print("You know it is the end, you pray one last time and then you are engulfed with flame. You lose 3 Hearts")
            Game_Over()
            
            
    B9 = False        
    
    while B9:
        wn.update()

    

BP7()


# Finish
turtle.resetscreen()

def BP9():
    wn.setup(width=400, height=200, startx=None, starty=None)
    wn.bgpic("C:\\Users\\Andre\\Downloads\\Dragon Folder\\BG10E.png")
    
    turt.speed(0)
    turt.pencolor("black")
    turt.penup()
    turt.goto(0,40)
    turt.pendown()
    turt.write("Congratulations Hero, you have recovered the Dragons Heart", move=False, align="center", font=("Arial", 8, "normal"))
    turt.penup()
    turt.goto(0,0)
    turt.pendown()
    turt.write(" along with a handful of the riches that came with it. ", move=False, align="center", font=("Arial", 8, "normal"))
    turt.penup()
    turt.goto(0,-40)
    turt.pendown()
    turt.write("Dragon's Heart Complete.", move=False, align="center", font=("Arial", 8, "normal"))

   
    print("Highest Score Possible: 1000")
    print("Total Score: ", sum(score))
   
    

BP9()




wn.mainloop()























