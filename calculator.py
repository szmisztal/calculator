import logging
logging.basicConfig(level=logging.DEBUG)

def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def divide (x, y):
    return x / y

while True:
    math_operation = input("Podaj działanie, posługując się odpowiednią liczbą: 1 - Dodawanie, 2 - Odejmowanie, 3 - Mnożenie, 4 - Dzielenie: ")
    if math_operation in ('1', '2', '3', '4'):
        try:
            num_x = float(input("Podaj pierwszą liczbę: "))
            num_y = float(input("Podaj drugą liczbę: "))
        except ValueError:
            print("Nieprawidłowa wartość. Musisz podać liczbę.")
            continue

        if math_operation == '1':
            logging.info(f"Dodaję {num_x} i {num_y}")
            print("Wynik to: ", addition(num_x, num_y), )

        elif math_operation == '2':
            logging.info(f"Odejmuję {num_y} od {num_x}")
            print("Wynik to: ", subtraction(num_x, num_y))

        elif math_operation == '3':
            logging.info(f"Mnożę {num_x} przez {num_y}")
            print("Wynik to: ", multiplication(num_x, num_y))

        elif math_operation == '4':
            logging.info(f"Dzielę {num_x} przez {num_y}")
            print ("Wynik to: ", divide(num_x, num_y))
    
        another_operation = input("Czy chcesz działać dalej ? 1 - Tak, 2 - Nie: ")
        if another_operation == '1':
            continue
        elif another_operation == '2':
            print("No to żegnam.")
            break
        else:
            print("Nieprawidłowa wartość.")
    else:
        print("Nieprawidłowa wartość.")

        
    
