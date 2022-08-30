class Alumnos:
    def __init__(self, nombre, apellido, dni):
        print("Alumno creado\n")
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

    def imprimirDatosAlumno(self):
        print("Nombre del alumno: " + self.nombre, "\nApellido del alumno: " 
+ self.apellido, "\nDni del alumno: " + self.dni + "\n")

alumnoCreado1 = Alumnos('Juan','Gluschancoff','36397169')
alumnoCreado2 = Alumnos('Luffy','Monkey','32983120')
alumnoCreado1.imprimirDatosAlumno()
alumnoCreado2.imprimirDatosAlumno()
