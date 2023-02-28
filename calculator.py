import logging
logging.basicConfig(level=logging.DEBUG)

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def divide (x, y):
    return x / y

while True:
    math_operation = input("Podaj działanie, posługując się odpowiednią liczbą: 1 - Dodawanie, 2 - Odejmowanie, 3 - Mnożenie, 4 - Dzielenie: ")
    if math_operation not in ('1', '2', '3', '4'):
        print("Niepoprawna wartość.")
        continue
    
    if math_operation == '1':
        numbers = []
        while True:
            try:
                number = float(input("Podaj liczbę: "))
            except ValueError:
                print("Niepoprawna wartość.")
                continue
            question = input("Czy chcesz dodać kolejną liczbę ? 1 - Tak, 2 - Nie: ")
            numbers.append(number)
            if question == '1':
                continue
            elif question == '2':
                all_numbers = sum(numbers)
                print("Wynik to: ", all_numbers)
                break
            elif question not in ('1', '2'):
                print("Niepoprawna wartość.")
                break

    elif math_operation == '2':
        try:
            num_x = float(input("Podaj pierwszą liczbę: "))
            num_y = float(input("Podaj drugą liczbę: "))
        except ValueError:
            print("Nieprawidłowa wartość. Musisz podać liczbę.")
            continue
        logging.info(f"Odejmuję {num_y} od {num_x}")
        print("Wynik to: ", subtraction(num_x, num_y))

    elif math_operation == '3':
        try:
            num_x = float(input("Podaj pierwszą liczbę: "))
            num_y = float(input("Podaj drugą liczbę: "))
        except ValueError:
            print("Nieprawidłowa wartość. Musisz podać liczbę.")
            continue
        logging.info(f"Mnożę {num_x} przez {num_y}")
        print("Wynik to: ", multiplication(num_x, num_y))

    elif math_operation == '4':
        try:
            num_x = float(input("Podaj pierwszą liczbę: "))
            num_y = float(input("Podaj drugą liczbę: "))
        except ValueError:
            print("Nieprawidłowa wartość. Musisz podać liczbę.")
            continue
        logging.info(f"Dzielę {num_x} przez {num_y}")
        print("Wynik to: ", divide(num_x, num_y))
    
    another_operation = input("Czy chcesz działać dalej ? 1 - Tak, 2 - Nie: ")
    if another_operation == '1':
        continue
    elif another_operation == '2':
        print("No to żegnam.")
        break
    else:
        print("Nieprawidłowa wartość.")
