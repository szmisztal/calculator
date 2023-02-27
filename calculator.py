import logging
logging.basicConfig(level=logging.DEBUG)

def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division (x, y):
    return x / y

math_operation = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
if math_operation == 1:
    addition
elif math_operation == 2:
    subtraction
elif math_operation == 3:
    multiplication
elif math_operation == 4:
    division

num_x = float(input("Podaj pierwszą liczbę: "))
num_y = float(input("Podaj drugą liczbę: "))