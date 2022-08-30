class Alumnos:
    def __init__(self, nombre, apellido, dni):
        print("Alumno creado")
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

alumno1 = Alumnos("Juan","Gluschancoff","36397169")
print(alumno1)



