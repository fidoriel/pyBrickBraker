import turtle
import random
import math

#-----------------------class Player------------------------
class Platform(turtle.Turtle): #Geerbt von Turtle
    #Konstruktor:
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.color("white")
        self.draw()
        self.hideturtle()

    def draw(self):
        pass

if __name__ == "__main__":
    #Bildschirm
    wn = turtle.Screen()
    wn.setup(600, 500) #Größe
    wn.bgcolor("black") #Farbe

    player = Platform()
    player.draw()