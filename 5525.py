import turtle
from random import randint

def strToInt(question="Value: ", val="", maxTries=10):
  if(val==""): val=input(question)
  try:
    c=int(val)
  except ValueError:
    print("Can\'t convert string to integer.")
    if(maxTries!=0):
      print("Try again!")
      if(maxTries==-1): c=strToInt()
      else: c=strToInt(maxTries=maxTries-1)
    else: c=False
  return c
mode=strToInt(question="Ar tu nori 3 spalvu ar 2?\nJei 2 ivesk \'0\';\nJei 3 ivesk \'1\'.\nPasirinkimas: ", maxTries=5)
generateExplodes=strToInt(question="Žaidimo sunkumas (geriausiai 5): ", maxTries=5)
if(not generateExplodes):
  generateExplodes=5

screen=turtle.getscreen()
turtle.hideturtle()
r=20
lines=5
rows=5
a=True
colors=["white", "red"]#, "green"]
values=[]
if(mode==1):
  colors.append("green")

#values=["0:2:0:2:1", "2:0:1:0:1", "2:1:1:0:0", "0:2:1:1:0", "1:0:0:0:2"]#5 linesand 5 rows inside
#colorsValues=[0, 2, 0, 2, 1, 2, 0, 1, 0, 0, 2, 1, 1, 0, 2, 0, 2, 1, 1, 0, 1, 0, 0, 0, 2]

#Preparing for play functions
def generateMonoList():
  global values
  values=[]
  for i in range(lines*rows):
    tmp=[]
    tmp.append(0)
    values.append(tmp)
def randomExplode(size=5, tracer=True):
  for i in range(size):
    num=randint(0, (rows*lines)-1)
    explode(num, tracer)
def rectangle(startX, startY, endX, endY):
  turtle.penup()
  turtle.goto(startX, startY)
  turtle.pendown()
  turtle.setx(endX)
  turtle.sety(endY)
  turtle.setx(startX)
  turtle.sety(startY)
def fullLoad(colorsl=True, xy=True, rectangles=True, reset=False):
  global values
  if(reset): turtle.reset()
  turtle.hideturtle()
  screen.tracer(0)
  i=0
  for y in range(r*lines, (r-1)*lines*(-1), (r+r)*(-1)):
    for x in range(r*rows*(-1), (r-1)*rows, r+r):
      tmp=values[i]
      if(xy):
        tmp.append(x)
        tmp.append(y)
        values[i]=tmp
      if(rectangles):
        rectangle(x, y, x+r+r, y-r-r)
        turtle.penup()
      if(colorsl):
        turtle.color(colors[values[i][0]])
        turtle.goto(x+r, y-r)
        turtle.dot(r)
        turtle.color("black")
      i+=1
  screen.tracer(1)
  screen.update()
def startup():
  global a
  #while(not isEnd()):
  generateMonoList()
  fullLoad(colorsl=False, rectangles=False)
  screen.tracer(0)
  randomExplode(tracer=False)
  fullLoad(xy=False, rectangles=False)
  if(a):
    fullLoad(colorsl=False, xy=False)
    a=False
  #turtle.exitonclick()
  screen._root.mainloop()
  #while(not isEnd()): pass
#Infomation manipulating functions
def getCurrentLine(i):
  global rows
  if(i==0): return 1.0
  a=i/rows
  b=round(a)
  if(a>b or a==round(a)): c=b+1
  else: c=b
  return c
def getCurrentRow(i):
  global rows
  if(rows>i):
    return i+1;
  else:
    currLine=getCurrentLine(i);
    return (rows-((rows*currLine)-i))+1
def getNextColor(id, edge=len(colors)-1, output="name"):
  colorID=values[id][0]
  if(colorID==edge):
    colorID=0
  else:
    colorID+=1
  if(output=="name"):
    return colors[colorID]
  else:
    return colorID
#Functions for real playing
def setColor(i):
  global values
  values[i][0]=getNextColor(i, output="id")
  color=colors[values[i][0]]
  turtle.color(color)
  x=values[i][1]+r
  y=values[i][2]-r
  turtle.penup()
  turtle.goto(x, y)
  turtle.dot(r)
def explode(i, tracer=True):
  setColor(i)
  currLine=getCurrentLine(i)
  currRow=getCurrentRow(i)
  if(tracer): screen.tracer(0)
  if(currRow!=1):
    #print("l")
    setColor(i-1)
  if(currRow!=rows):
    #print("r")
    setColor(i+1)
  if(currLine!=1):
    #print("u")
    setColor(i-rows)
  if(currLine!=lines):
    #print("d")
    setColor(i+rows)
  if(tracer): screen.tracer(1)

def click(x, y):
  fullLoad(xy=False, reset=True)
  if(isEnd()): startup()
  global values
  for i in range(len(values)):
    tmp=values[i]
    if(x>tmp[1] and x<(tmp[1]+r+r) and y<tmp[2] and y>(tmp[2]-r-r)):
      explode(i)
      if(isEnd()): print("Baigta")
      break
def isEnd(value=0):
  end=True
  for i in values:
    if(i[0]!=value):
      end=False
  return end

screen.onclick(click)
startup()
