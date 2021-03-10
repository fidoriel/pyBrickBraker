
import turtle
import random
import math

#Bildschirm
wn = turtle.Screen()
wn.setup(400,400) #Größe
wn.bgcolor("black") #Farbe

class Border(turtle.Turtle): #Geerbt von Turtle
    def __init__(self):
        #Konstruktor:
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.pensize(2)
    
    #Vor.: keine
    #Effekte: Die Spielfeldgrenze ist gezeichnet.
    def draw(self):
        self.penup()
        self.goto(-150,-150)
        self.pendown()
        self.goto(150,-150)
        self.goto(150,150)
        self.goto(-150,150)
        self.goto(-150,-150)

border = Border()
border.draw()