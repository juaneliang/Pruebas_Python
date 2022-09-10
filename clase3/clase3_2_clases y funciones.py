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

alumno = Alumnos.agregarAlumno()
alumno.imprimirDatosAlumno()