#funciones de orden superior

#funcione que suma 100
from multiprocessing.sharedctypes import Value


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

numeros = [7,2,3]
numeros_cuadrados = list(map(lambda x: x**2, numeros))
print(numeros_cuadrados)

for i in numeros_cuadrados:
    print(i)

#ejercicio 1: Orden superior // funcion superior que eleve al cubo

def elevaCubo(x):
    return x**3

print(superior(elevaCubo, [3,6,8]))

#sort para ordenar listas
print(numeros_cuadrados.sort(),
" // el none esta OK, porque solo lo ordena, y luego muestro como queda: //",
numeros_cuadrados)