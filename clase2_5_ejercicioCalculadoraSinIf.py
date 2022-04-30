while True:
    try:
        num_1 = float(input("Escribe un numero"))
        num_2 = float(input("Escribe otro numero"))
        print(num_1 + num_2)
        print(num_1 + num_2)
        print(num_1 + num_2)
        print(num_1 + num_2)
    except ValueError:
        print("Eso no es un numero... Reingrese!")
    except ZeroDivisionError:
        print("No se puede dividir por 0")
    else:
        break

