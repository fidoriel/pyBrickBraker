# -*- coding: utf-8 -*-
import turtle
import random
import math
from time import sleep
debug = True

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

#-----------------------class Platform------------------------
class Platform( turtle.Turtle ): #Geerbt von Turtle
    #Konstruktor:
    def __init__( self ):
        turtle.Turtle.__init__( self )
        self.penup()
        self.color( "white" )
        self.hideturtle()

        self.isFrozen = False
        self.width = 60

        self.position = [ self.width/-2, -200 ]
        # border L and R
        self.maxLeft = -250
        self.maxRight = 250
        # speed
        self.sensitivity = 10
        self.speed(0)

    def draw( self ):
        if debug: print( self.position[ 0 ] )
        self.goto( self.position[ 0 ], self.position[ 1 ] )
        self.pendown()

        for i in range( 2 ):
          self.forward( self.width )
          self.right( 90 )
          self.forward( 10 )
          self.right( 90 )

        self.penup()

    def setPotitionAndRefresh( self, x, y ):
        self.position = [ x, y ]
        self.refresh()

    def refresh( self ):
        self.clear()
        self.draw()

    def moveR( self ):
      if ( self.position[ 0 ] + self.width ) < self.maxRight:
        if not self.isFrozen and self.doesNotTouchBorder():
            self.position[ 0 ] += self.sensitivity
        if debug: print( "move r" )
        self.refresh()

    def moveL( self ):
      if self.position[ 0 ] > self.maxLeft:
        if not self.isFrozen and self.doesNotTouchBorder():
            self.position[ 0 ] -= self.sensitivity
        if debug: print( "move l" )
        self.refresh()

    def doesNotTouchBorder( self ):
        return True

def main():
    #Bildschirm
    field = turtle.Screen()
    field.setup(600, 500) #Größe
    field.bgcolor("black") #Farbe
    
    ball = Ball()

    platform = Platform()
    platform.draw()

    field.listen()

    # regular OS key codes
    #field.onkey( platform.moveL, "Left" )
    #field.onkey( platform.moveR, "Right" )

    # python sculpt implementation KeyCodes
    field.onkey( platform.moveL, "LEFT" )
    field.onkey( platform.moveR, "RIGHT" )
    field.tracer( 0 )

    while True:
        field.update()
        ball.move()
        
        sleep( 0.01 )
  
if __name__ == "__main__":
  main()
