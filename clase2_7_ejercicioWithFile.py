from asyncio.windows_events import NULL
from datetime import date, datetime
from encodings import utf_8
from fileinput import close
from msilib.schema import Class

class Files:
    def __init__(self, nombre, apellido, dni):
        print("\nAlumno creado\n")
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

#No hace falta usar el .close()

#MI PC
#'C:\\Programacion\\Python\\Pruebas_Python\\clase2_7_ejercicioTestTxt.txt'
#TRABAJO PC
#'C:\\Repositories\\Pruebas_Python2\\clase2_7_ejercicioTestTxt.txt'

    archivoALeer = 'C:\\Repositories\\Pruebas_Python2\\clase2_7_ejercicioTestTxt.txt'

#Funcion con with para recorrer el archivo
    def vaciarArchivo(archivoALeer):
        with open(archivoALeer, 'w', encoding='utf-8') as archivo:
            return archivoALeer

#Funcion con with para recorrer el archivo
    def leerArchivo(archivoALeer):
        try:
            with open(archivoALeer, encoding='utf-8') as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    print(linea)
            return linea
        except UnboundLocalError:
            print("El archivo esta vacio\n")

#Funcion con with para escribir el archivo y agrega fecha de hoy por cada cadena de string
    def escribirYLoguearArchivo(archivoALeer,escribir):
        with open(archivoALeer, 'a', encoding='utf-8') as archivo:  
            archivo.write(datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + " " + escribir + "\n")

#Opciones
    print("1_Vaciar Archivo --> Deshabilitado\n")
    print("2_Leer Archivo \n")
    print("3_Escribir Archivo \n")
    print("0_Salir \n")

#Seteo de variable opcion
    opcion = NULL

    while opcion != '0':
            opcion = input("\nIngresar la opcion deseada: \n")
            #if opcion == '1':
                #Vaciar archivo
                #vaciarArchivo(archivoALeer)
            if opcion == '2':
                #Recorrer archivo primera vez
                leerArchivo(archivoALeer)
            if opcion == '3':
                escribir = input("Escribir que desea agregar en el archivo: \n")
                escribirYLoguearArchivo(archivoALeer,escribir)
#Cerrar programa
    close()