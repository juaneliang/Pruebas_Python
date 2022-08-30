from pydoc import importfile
from re import A

class Alumnos:
    def __init__(self, nombre, apellido, dni):
        print("\nAlumno creado\n")
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

    def imprimirDatosAlumno(self):
        print("Nombre del alumno: " + self.nombre, "\nApellido del alumno: " 
+ self.apellido, "\nDni del alumno: " + self.dni + "\n")

    def agregarAlumno():
        nombre = input("\nIngresar nombre del alumno: ")
        apellido = input("\nIngresar apellido del alumno: ")
        dni = input("\nIngresar dni del alumno: ")
        alumno = Alumnos(nombre, apellido, dni)
        return alumno

#alumnoCreado1 = Alumnos('Juan','Gluschancoff','36397169')
#alumnoCreado2 = Alumnos('Luffy','Monkey','32983120')
alumno = Alumnos.agregarAlumno()
alumno.imprimirDatosAlumno()