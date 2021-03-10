
import turtle
import random
import math

#Bildschirm
wn = turtle.Screen()
wn.setup(400,400) #Größe
wn.bgcolor("black") #Farbe

class Border(turtle.Turtle): #Geerbt von Turtle
    def __init__(self, leftBorder, rightBorder, topBorder, bottomBorder):
        #Konstruktor:
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.pensize(2)
        self.leftBorder = leftBorder #-180
        self.rightBorder = rightBorder #180
        self.topBorder = topBorder #180
        self.bottomBorder = bottomBorder #-200
    
    #Vor.: keine
    #Effekte: Die Spielfeldgrenze ist gezeichnet.
    def draw(self):
        self.penup()
        self.goto(self.leftBorder,self.bottomBorder)
        self.goto(self.rightBorder,self.bottomBorder)
        self.pendown()
        self.goto(self.rightBorder,self.topBorder)
        self.goto(self.leftBorder,self.topBorder)
        self.goto(self.leftBorder,self.bottomBorder)

border = Border(-180, 180, 180, -200)
border.draw()