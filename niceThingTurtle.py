import turtle as t
from time import sleep

x=200#pagrindinis ornamento dydis
colors=["black", "green", "blue", "red"]#spalvos naudojamos ornamente

def drawRectangle(x):#programa kvadrato nupiesimui
	for rotate in range(4):
		t.forward(x)
		t.left(90)

#t.reset()
#t.penup()
#t.setx(-(x/2))
#t.sety(x/2)
#t.pendown()

#t.speed(10)#nustatomas greitis
t.tracer(0)

for a in range(int(360/len(colors)/4)):#sis ciklas bus kartojamas kol ornamentas apsisuks 360 laispniu
	print("Ciklas: " + str(a+1))
	for c in colors:#ornamente panaudojama visos spalvos sarase colors
		print("Spalva: " + c)
		t.color(c)
		for i in range(4):#piesiamas originalus ornamentas!
			t.forward(x)
			drawRectangle(x/4)
			t.right(90)
		#t.penup()
		#t.forward(x/10)
		#t.right(90)
		#t.forward(x/10)
		#t.left(90+5)
		#t.pendown()
		t.left(4)
	t.left(1)

t.tracer(1)

sleep(120)
