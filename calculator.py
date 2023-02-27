import sys
import logging
logging.basicConfig(level=logging.DEBUG)

def addition(x, y):
    logging.info(f"Dodaję {num_x} i {num_y}")
    return x + y

def subtraction(x, y):
    logging.info(f"Odejmuję {num_y} od {num_x}")
    return x - y

def multiplication(x, y):
    logging.info(f"Mnożę {num_x} przez {num_y}")
    return x * y

def division (x, y):
    logging.info(f"Dzielę {num_x} przez {num_y}")
    return x / y

math_operation = input("Podaj działanie, posługując się odpowiednią liczbą: 1 - Dodawanie, 2 - Odejmowanie, 3 - Mnożenie, 4 - Dzielenie: ")

if math_operation == '1':
    num_x = float(input("Podaj pierwszą liczbę: "))
    num_y = float(input("Podaj drugą liczbę: "))
    print("Wynik to: ", addition(num_x, num_y), )

elif math_operation == '2':
    num_x = float(input("Podaj pierwszą liczbę: "))
    num_y = float(input("Podaj drugą liczbę: "))
    print("Wynik to: ", subtraction(num_x, num_y))

elif math_operation == '3':
    num_x = float(input("Podaj pierwszą liczbę: "))
    num_y = float(input("Podaj drugą liczbę: "))
    print("Wynik to: ", multiplication(num_x, num_y))

elif math_operation == '4':
    num_x = float(input("Podaj pierwszą liczbę: "))
    num_y = float(input("Podaj drugą liczbę: "))
    print ("Wynik to: ", division(num_x, num_y))

else:
    print("Niepoprawna wartość.")
    


