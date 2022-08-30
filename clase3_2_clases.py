class Alumnos:
    def __init__(self, nombre, apellido, dni):
        print("Alumno creado")
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

alumno1 = Alumnos('Juan','Gluschancoff','36397169')
print("Nombre del alumno: " + alumno1.nombre, "\nApellido del alumno: " 
+ alumno1.apellido, "\nDni del alumno: " + alumno1.dni)

