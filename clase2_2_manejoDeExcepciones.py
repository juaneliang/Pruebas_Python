#manejo de excepciones

#yendo por el eexcept
try:
    int("hola mundo")
except (ValueError, TypeError):
    print("Eso no es un numero.")
else:
    print("todo salio bien!")
#yendo por el else
try:
    int(2)
except (ValueError, TypeError):
    print("Eso no es un numero.")
else:
    print("todo salio bien!")





