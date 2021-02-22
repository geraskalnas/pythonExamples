from random import randint

print "Calling python.\n"
#Celsius = int(raw_input("Enter a temperature in Celsius: "))
Celsius=randint(-30, 100)
#Celsius=19
Fahrenheit = 9.0/5.0 * Celsius + 32

print "Temperature:", Celsius, "C = ", Fahrenheit, " F"

Fahrenheit=randint(-30, 100)
#Fahrenheit = 66.2
Celsius = (Fahrenheit - 32) * (5.0/9.0)

print "Temperature:", Fahrenheit, "F = ", Celsius, " C"

print "\nCompleted successfully."