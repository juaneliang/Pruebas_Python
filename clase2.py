#funciones de orden superior

#funcione que suma 100
def sumarCien(x):
    return x+100
#funcione que eleva al cuadrado
def elevaCuadrado(x):
    return x**2
#funcion superior que anexa otra funcion
def superior(funcion,lista):
    resultado = []
    for n in lista:
        resultado.append(funcion(n))
    return resultado

#devuelve una lista sumandole Cien/100
print(superior(sumarCien,[3,6,8]))
#devuelve una lista elevando al cuadrado
print(superior(elevaCuadrado,[3,6,8]))

#funciones lambda 

print(superior(lambda x: x**2, [3,6,8]))
