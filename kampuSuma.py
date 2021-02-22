from turtle import *
n = 0
while not n == 1 :
    print ('Figūros kampų sumos skaičiuoklė')
    print('Iveskite \'1\' noredami baigti.')
    n = int(input('Įveskite kampų skaičių: '))
    if n == 1:
        break
    else:
        print ('Kompiuteris galvoja...')
        print ('Kompiuteris skaičiuoja...')
        laik = n - 2
        atsakymas = laik * 180
        print (n, '- kampio kampų suma:', atsakymas)
        kampas = 360 / n
        reset()
        for i in range(n):
            forward(100)
            right(kampas)
