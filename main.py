import turtle
import random
import math

#-----------------------class Ball------------------------
class Ball(turtle.Turtle): #Geerbt von Ball
    # Konstruktor:
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(1)
        self.color("white")
        self.shape("circle")
        self.speed = 3 #zusätzliches Attribut
        self.setheading(random.randint(0,360))

    #Vor.: Der Ball befindet sich innerhalb des Spielfeldes.
    #Effekte: Der Ball wurde speed-Pixel in Blickrichtung vorwärts bewegt und ist an den Grenzen des Spielfeldes gedreht worden.
    def move(self):
        self.forward(self.speed)

        if self.xcor() > 150 or self.xcor() < -150:
            self.left(60)
        if self.ycor() < -150 or self.ycor() > 150:
            self.left(60)

#Erzeuge Instanzen der Klassen
if __name__ == "__main__":
    #Bildschirm
    wn = turtle.Screen()
    wn.setup(400,400) #Größe
    wn.bgcolor("blue") #Farbe
    ball = Ball()
    while True:
        ball.move()