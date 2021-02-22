from tkinter import *
from random import randint
print(',,Mesk kauliuka" programa')
minx = int(input('Maziausias skaicius:'))
maxx = int(input('Didziausias skaicius:'))
def roll():
    text.delete(0.0, END)
    text.insert(END, str(randint(minx, maxx)))
window = Tk()
window.title('Mesk kauliuka')
text = Text(window, width=1, height=1)
buuton = Button(window, text='Ismesti', command = roll)
text.pack()
buuton.pack()
