from ctypes.wintypes import HLOCAL

#variables
a = 32
b = 23
resultado = a + b
#mostrar en pantalla
print (resultado)

#listas
lista = [1, "hola", 1.6]
#mostrar lista
print (lista)
#limpiar lista
lista.clear()
#mostrar lista
print (lista)
#agregar variables en general, no se puede agregar mas de 1 a la vez
lista.append(11)
lista.append("holaotravez")
lista.append(2.0)
#mostrar lista
print (lista)

#tupla lista que no se puede modificar
tupla = [2, "holatupla", 1.8]
#mostrar tupla
print (tupla)

#set de datos es para no tener duplicados
set_datos = {2,3,4,6}
#mostrar set de datos
print (set_datos)

#diccionario
diccionario = {"a":"hola", "b":"mundo", "c":11}
#mostrar diccionario
print (diccionario)
#modificar valor en variable del diccionario
diccionario["a"] = "chau"
#mostrar diccionario
print (diccionario)

#del para borrar en general variables
del diccionario["a"]
#mostrar diccionario
print (diccionario)

#negacion con print para mostrar
print (a is not None)
#negacion en variable y mostrar
resultado = a is not None
print (resultado)
#verdadero con print para mostrar
print (a is None)
#verdadero en variable y mostrar
resultado = a is None
print (resultado)

#in prueba
resultado = 6 in tupla
print (resultado)
resultado = 1.8 in tupla
print (resultado)

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

#while, / 0 a 9, se forza a que sea un int
a = int(input("ingresa numero para comenzar para loop: "))
b = int(input("ingresa numero para terminar loop: "))
while a < b:
    print(a)
    a += 1

#for clasico, recorre 5 iterasiones
for i in range(5):
    print("iterasion", i + 1)

#for each, saltea el numero 10
numeros = [2,4,6,10,8,9]
for numero in numeros:
    if numero == 10: continue
    print(numero)

#ejercicio sumatoria
#for each que cuenta todos menos el ultimo valor de la lista
#por eso se pone el len osea el tamanio de la lista -1
numeros2 = [2,4,6,10,8,9]
suma = 0
for i in range(len(numeros2)-1):
    suma += numeros2[i]
print(suma)

#ejercicio mostrar y eliminar, while y del
while numeros:
    print (numeros)
    del numeros[-1]
    print (numeros)

#################################################################

#funciones
#no devuelven un resultado
def imprimirAlgo(mensaje):
    for caracter in mensaje:
        print (caracter)

#devuelven resultado
mensaje = input("Escribi un mensaje: ")
imprimirAlgo(mensaje)

#funcion resta
def resta(a,b):
    return a-b

a = int(input("valor del primer numero: "))
b = int(input("valor del segundo numero: "))
resultadoResta = resta(a,b)
print(resultadoResta)

