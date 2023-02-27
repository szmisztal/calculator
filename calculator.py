import logging
logging.basicConfig(level=logging.DEBUG)

math_operation = input("Podaj działanie, posługując się odpowiednią liczbą: 1 - Dodawanie, 2 - Odejmowanie, 3 - Mnożenie, 4 - Dzielenie: ")

def choice():
    num1 = float(input("Podaj pierwszą liczbę: "))
    num2 = float(input("Podaj drugą liczbę: "))
    if True:
        pass
    else:
        print("To nie jest liczba")
    return num1, num2
choice()    

num_x = num1
num_y = num2

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

if math_operation == '1':
    print("Wynik to: ", addition(num_x, num_y), )
elif math_operation == '2':
    print("Wynik to: ", subtraction(num_x, num_y))
elif math_operation == '3':
    print("Wynik to: ", multiplication(num_x, num_y))
elif math_operation == '4':
    print ("Wynik to: ", division(num_x, num_y))

