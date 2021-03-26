# -*- coding: utf-8 -*-

import turtle
import random
import math
from time import sleep, time
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
        self.speed = 1 #zusätzliches Attribut
        self.goto( 0, 100 )
        self.setheading(random.randint(0,360))

    #Vor.: Der Ball befindet sich innerhalb des Spielfeldes.
    #Effekte: Der Ball wurde speed-Pixel in Blickrichtung vorwärts bewegt und ist an den Grenzen des Spielfeldes gedreht worden.
    def move(self):
        self.forward(self.speed)
    
    #Vor.: Keine
    #Effekte: Drehe um 60 grad nach links.
    def objTouch( self ):
        self.left( random.randint( 50, 70 ) )

#-----------------------class Brick------------------------
class Brick(turtle.Turtle): #Geerbt von Turtle
    # Konstruktor:
    def __init__( self, x, y ):
        turtle.Turtle.__init__( self,  )
        self.hideturtle()
        self.penup()
        self.speed(0)

        self.healthpoints = 4
        self.colorPoints = { 4: "white", 3: "green", 2: "yellow", 1: "red" }
        self.lastCollision = time() * 10000

        self.position = [ x, y ]
        # Breite x Laenge
        self.size = [ 60, 30 ]

    #Vor.: keine
    #Effekte: Der Brick ist an der Position self.position gezeichent.
    def draw( self ):
        self.color( self.colorPoints[ self.healthpoints ] )
        if debug: print( self.position[ 0 ] )
        self.goto( self.position[ 0 ], self.position[ 1 ] )
        self.pendown()

        for i in range( 2 ):
          self.forward( self.size[ 0 ] )
          self.right( 90 )
          self.forward( self.size[ 1 ] )
          self.right( 90 )

        self.penup()
    
    #Vor.: keine
    #Effekte: Wenn der Ball den Brick berührt hat, ist der Brick nicht mehr sichtbar.
    def collision( self, ball ):
        #stretch_wid, stretch_len, outlinewidth = ball.turtlesize()
        dist = 10 #* stretch_len
        #print( time() * 1000 )
        if time() * 10000 - self.lastCollision > 80:
            if self.healthpoints != 0:
                if self.ycor() >=  ( ball.ycor() - dist ) >= ( self.ycor() - self.size[ 1 ] ) or self.ycor() >=  ( ball.ycor() + dist ) >= ( self.ycor() - self.size[ 1 ] ):
                    if self.xcor() <= ( ball.xcor() - dist ) <= ( self.xcor() + self.size[ 0 ] ) or self.xcor() <= ( ball.xcor() + dist ) <= ( self.xcor() + self.size[ 0 ] ): 

                        if debug:
                            print( "collision" )
                            print( ball.xcor(), ball.ycor() )
                        # print( ball.shapesize() )

                        ball.objTouch()
                        self.healthpoints -= 1

                        if debug: print( self.healthpoints )

                        if not self.healthpoints:
                            self.clear()
                            return True

                        else:
                            self.draw()
                            return True
        
        self.lastCollision = time() * 10000
        return False

#-----------------------class Border------------------------
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
    
    #Vor.: keine
    #Effekte: Wenn der Ball unter der Plattform ist, ist er in die Mitte des Spielfeldes gesetzt.
    def collision( self, ball ):
        #stretch_wid, stretch_len, outlinewidth = ball.turtlesize()
        dist = 10# * stretch_len
        if ball.ycor() <= self.bottomBorder:
            if debug: print( "fallout" )
            ball.goto( 0, 0 )
        
        elif ball.xcor() < self.leftBorder or ball.xcor() > self.rightBorder:
            ball.objTouch()

        elif ball.ycor() > self.topBorder:
            ball.objTouch()

#-----------------------class Platform------------------------
class Platform( turtle.Turtle ): #Geerbt von Turtle
    #Konstruktor:
    def __init__( self, borders ):
        turtle.Turtle.__init__( self )
        self.penup()
        self.color( "white" )
        self.hideturtle()

        self.isFrozen = False
        self.width = 120

        self.position = [ self.width/-2, ( -borders + 10 ) ]
        # border L and R
        self.maxLeft = -borders
        self.maxRight = borders
        # speed
        self.sensitivity = self.width/2
        self.speed(0)

    #Vor.: Keine
    #Effekte: Die Plattform wird gezeichnet.
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

    #Vor.: Keine
    #Effekte: Die Position wird geändert und die Plattform wird aktualisiert
    def setPotitionAndRefresh( self, x, y ):
        self.position = [ x, y ]
        self.refresh()

    #Vor.: setPotitionAndRefresh wurde ausgeführt
    #Effekte: Die Plattform wird entfernt und neu gezeichnet
    def refresh( self ):
        self.clear()
        self.draw()

    #Vor.: Keine
    #Effekte: Die Plattform bewegt sich nach rechts
    def moveR( self ):
      if ( self.position[ 0 ] + self.width ) < self.maxRight:
        if not self.isFrozen and self.doesNotTouchBorder():
            self.position[ 0 ] += self.sensitivity
        if debug: print( "move r" )
        self.refresh()

    #Vor.: Keine
    #Effekte: Die Plattform bewegt sich nach links
    def moveL( self ):
      if self.position[ 0 ] > self.maxLeft:
        if not self.isFrozen and self.doesNotTouchBorder():
            self.position[ 0 ] -= self.sensitivity
        if debug: print( "move l" )
        self.refresh()

    #Vor.: Berührt die Grenze
    #Effekte: Gebe True aus
    def doesNotTouchBorder( self ):
        return True
    
    #Vor.: Keine
    #Effekte: Teste ob der Ball und die Plattform sich berühren
    def collision( self, ball ):
        #stretch_wid, stretch_len, outlinewidth = ball.turtlesize()
        dist = 10# * stretch_len
        if ( ball.ycor() - dist ) <= self.ycor() or ( ball.ycor() + dist ) <= self.ycor():
            if self.xcor() <= ( ball.xcor() - dist ) <= ( self.xcor() + self.width ) or self.xcor() <= ( ball.xcor() + dist ) <= ( self.xcor() + self.width ):
                if debug: print( "collision" )
                ball.objTouch()

#-----------------------class Score------------------------
class Score(turtle.Turtle): #Geerbt von Turtle
    def __init__(self, height):
        #Konstruktor:
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.pensize( 10 )
        self.score = 0
        self.height = height
    #Vor.: keine
    #Effekte: Die Spielfeldgrenze ist gezeichnet.
    def draw(self):
        self.penup()
        self.goto(0,self.height)
        
        self.write((self.score), align = "center", font = ("impact", 30, "normal"))

    #Vor.: keine
    #Effekte: Fügt dem Score 10 hinzu und zeichnet ihn neu
    def update(self,points):
        self.clear()
        self.score += points
        self.draw()

    #Vor.: keine
    #Effekte: Fügt mehrere Bricks ein.
class Bricks():
    def __init__( self, rows, cols ):
        self.bricksList = [ [ ] for _ in range( rows ) ]

        y = 230
        for row in range( rows ):
            x = -205
            for col in range( cols ):
                self.bricksList[ row ].append( Brick( x, y ) )
                x += 70
            y -= 40
        
        self.draw()

    # Vor.: Keine
    # Effekte: Die Bricks sind gezeichnet
    def draw( self ):
        for row in self.bricksList:
            for brick in row:
                brick.draw()

    # vor.: Keine
    # Effekte: Der Brick verliert ein Leben wenn der Ball ihn berührt.
    def collision( self, ball, score ):
        for row in self.bricksList:
            for brick in row:
                if brick.collision( ball ) == True:
                    score.update(100)

def main():
    #Bildschirm
    field = turtle.Screen()
    field.setup(800, 800) #Größe
    field.bgcolor("black") #Farbe
    
    ball = Ball()

    border = Border(-300, 300, 300, -300)
    border.draw()

    platform = Platform( 300 )
    platform.draw()

    field.listen()

    # regular OS key codes
    field.onkey( platform.moveL, "Left" )
    field.onkey( platform.moveR, "Right" )

    # python sculpt implementation KeyCodes
    #field.onkey( platform.moveL, "LEFT" )
    #field.onkey( platform.moveR, "RIGHT" )
    field.tracer( 0 )

    bricks = Bricks( 4, 6 )
    
    score = Score( 330 )
    score.draw()

    while True:
        field.update()
        ball.move()
        platform.collision( ball )
        border.collision( ball )
        bricks.collision( ball, score )
        
        sleep( 0.001 )

  
if __name__ == "__main__":
    main()
