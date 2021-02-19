# -*- coding: utf-8 -*-
import turtle
import random
import math

#-----------------------class Player------------------------
class Platform( turtle.Turtle ): #Geerbt von Turtle
  #Konstruktor:
  def __init__( self ):
    turtle.Turtle.__init__( self )
    self.penup()
    self.color( "white" )
    self.draw()
    self.hideturtle()
    self.position = ( 0, 0 )
    self.sensitivity = 1
    self.speed(0)

  def draw( self ):
    pass
  
  def setPotitionAndRefresh(self, x, y):
    self.position = ( x, y )
    self.clear()
    self.draw()

  def moveR():
    pass
  
  def moveL():
    pass

def main():
  player = Platform()
  player.draw()
  
  #Bildschirm
  wn = turtle.Screen()
  wn.setup(600, 500) #Größe
  wn.bgcolor("black") #Farbe

  wn.listen()
  wn.onkey( player.moveR, "LEFT" )
  wn.onkey( spieler.moveR, "RIGHT" )

  while True:
    wn.update()

if __name__ == "__main__":
  main()
  