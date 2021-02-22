from time import sleep
while True:
    print ('Lygčių Skaičiuoklė')
    print ('"Lygčių Skaičiuoklė" startuoja!')
    print ('Jei skaičius nėra sveikas tai vietoje kablelio rašykite tašką.')
    print ('Būtinai rašykite skaičių, nes priešingu atveju jums reikės paleisti programą iš naujo.')
    print ('INFO: a = 1 skaičius;    b = 2 skaičius;    x = nežinomas')
    a = int(input('a = '))
    b = int(input('b = '))
    print ('a) atvejis: x+a=b')
    print ('b) atvejis: a+x=b')
    atvejis = input('Įveskite atvejio raidę: ')
    if atvejis == 'a':
        print ('a) x+a=b')
        print ('b) x-a=b')
        print ('c) x*a=b')
        print ('d) x/a=b')
        aveiksmas = input('Įveskite veiksmo raidę: ')
        if aveiksmas == 'a':
            print ('Kompiuteris galvoja...')
            print ('Formulė: B - A = X')
            print ('Kompiuteris skaičiuoja...')
            c = b - a
            print ('x +', a, '=', b)
            print ('x =', b, '-', a)
            print ('x =', c)
            sleep (6)
            l = input ('Ar norite toliau skaičiuoti(taip/ne): ')
        elif aveiksmas == 'b':
            print ('Kompiuteris galvoja...')
            print ('Formulė: A - B = X')
            print ('Kompiuteris skaičiuoja...')
            c = a - b
            print ('x -', a, '=', b)
            print ('x =', a, '-', b)
            print ('x =', c)
            sleep (6)
        elif aveiksmas == 'c':
            print ('Kompiuteris galvoja...')
            print ('Formulė: B / A = X')
            print ('Kompiuteris skaičiuoja...')
            c = b / a
            print ('x *', a, '=', b)
            print ('x =', b, '/', a)
            print ('x =', c)
            sleep (6)
        elif aveiksmas == 'd':
            print ('Kompiuteris galvoja...')
            print ('Formulė: A * B = X')
            print ('Kompiuteris skaičiuoja...')
            c = a * b
            print ('x /', a, '=', b)
            print ('x =', b, '*', a)
            print ('x =', c)
            sleep (6)
        else:
            print ('Klaida!')
            print ('Lauk 1')
            sleep (1)
            print ('Lauk 1')
    elif atvejis == 'b':
        print ('a) a+x=b')
        print ('b) a-x=b')
        print ('c) a*x=b')
        print ('d) a/x=b')
        bveiksmas = input ('Įveskite veiksmo numerį: ')
        if bveiksmas == 'a':
            print ('Kompiuteris galvoja...')
            print ('Formulė: B - A = X')
            print ('Kompiuteris skaičiuoja...')
            c = b - a
            print (a, '+ x', '=', b)
            print ('x =', b, '-', a)
            print ('x =', c)
            sleep (6)
        elif bveiksmas == 'b':
            print ('Kompiuteris galvoja...')
            print ('Formulė: A - B = X')
            print ('Kompiuteris skaičiuoja...')
            c = a - b
            print (a, '- x =', b)
            print ('x =', a, '-', b)
            print ('x =', c)
            sleep (6)
        elif bveiksmas == 'c':
            print ('Kompiuteris galvoja...')
            print ('Formulė: B / A = X')
            print ('Kompiuteris skaičiuoja...')
            c = b / a
            print (a, '* x =', b)
            print ('x =', b, '/', a)
            print ('x =', c)
            sleep (6)
        elif bveiksmas == 'd':
            print ('Kompiuteris galvoja...')
            print ('Formulė: A / B = X')
            print ('Kompiuteris skaičiuoja...')
            c = a / b
            print (a, '/ x =', b)
            print ('x =', b, '-', a)
            print ('x =', c)
            sleep (6)
        else:
            print ('Klaida!')
            print ('Lauk 1')
            sleep (1)
            break
    else:
        print ('Klaida!')
        print ('Lauk 1')
        sleep (1)
        break