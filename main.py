# -*- coding: utf-8 -*-
import turtle
import random
import math
from time import sleep

# debug flag
debug = True

#-----------------------class Platform------------------------
class Platform( turtle.Turtle ): #Geerbt von Turtle
  #Konstruktor:
  def __init__( self ):
    turtle.Turtle.__init__( self )
    self.penup()
    self.color( "white" )
    self.hideturtle()

    self.position = [ 0, 0 ]
    self.sensitivity = 1
    self.speed(0)
    self.isFrozen = False

  def draw( self ):
    if debug: print( self.position[ 0 ] )
    self.goto( self.position[ 0 ], self.position[ 1 ] )
    self.pendown()
    self.forward( 50 )
    self.right( 90 )
    self.forward( 10 )
    self.right( 90 )
    self.forward( 50 )
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
    if not self.isFrozen and self.doesNotTouchBorder():
      self.position[ 0 ] += self.sensitivity
      if debug: print( "move r" )
      self.refresh()
  
  def moveL( self ):
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

  platform = Platform()
  platform.draw()

  field.listen()
  field.onkey( platform.moveL, "LEFT" )
  field.onkey( platform.moveR, "RIGHT" )
  field.tracer( 0 )

  while True:
      field.update()
      sleep( 0.01 )
  
if __name__ == "__main__":
  main()