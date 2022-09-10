paises = {
    "ar":"Argentina",
    "br":"Brasil",
    "us":"Estados unidos",    
    "es":"España",
}

while True:
    paisSeleccionado = input("elegir un codigo de pais: ")
    if paisSeleccionado == 'salir': break
    try:
        print(paises[paisSeleccionado])
    except KeyError:
        print("El codigo no existe!, ingresar un codigo correcto: ")
    else:
        break
