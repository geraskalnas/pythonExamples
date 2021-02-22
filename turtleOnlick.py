import random
from turtle import *
reset()
X=[]
Y=[]
kiek = 0
pakeisti=7
spalvos=["green", "red", "yellow", "blue", "purple", "pink"]


def saudom(x, y):
  goto(x, y)
  if(not isdown()): pendown()
  dot(5)

  global kiek, X, Y, pakeisti, spalvos
  kiek = kiek + 1
  write( kiek )
  X.append(x)
  Y.append(y)
  num=kiek/pakeisti
  if(str(num)[-1]=="0"):
  #if(not "." in str(kiek/pakeisti)):
    color(random.choice(spalvos))
    penup()
    for i in range(len(X)-pakeisti, len(X)):
      goto(X[i], Y[i]*-1)
      if(not isdown()): pendown()
      dot(5)
    penup()
    color(random.choice(spalvos))
screen = getscreen()
screen.onclick( saudom )

penup()
speed(0)
hideturtle()
