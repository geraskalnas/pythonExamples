'''
Created on 2016-04-15

@author: nojus
'''
from random import randint
from turtle import *
c = int(input('Kiek kartoti: '))
d = 0
for i in range(1, c+1):
    a = randint(20, 50)
    b = randint(1, 360)
    forward (a)
    left (b)
    d = d + 1
    e = c - i
    print ('Kartas: ', i, 'Is: ', c, 'Liko:', e)
    print ('Priekin: ', a)
    print ('Kairen:  ', b)
    print ('- - - - - - - - - - - - - - -')
