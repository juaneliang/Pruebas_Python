#input para ingresar valor de variable e if/else/elif
clima = input("como esta el clima?: ")
if clima == 'lluvia':
    dinero = int(input("de cuanto dinero dispones?: "))
    if dinero > 300:
        print("me tomo un taxi")
    else: 
        print("me tomo el colectivo")
elif clima == 'nublado':
    print("me voy caminando con cuidado")
else:
    print("me voy caminando")
print("termino el programa")