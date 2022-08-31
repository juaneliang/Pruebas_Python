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

#in prueba
resultado = 6 in tupla
print (resultado)
resultado = 1.8 in tupla
print (resultado)