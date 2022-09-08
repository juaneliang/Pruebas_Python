from persona import Persona

class Empleado(Persona):
    def __init__(self, sector, puesto):
        self.sector = sector
        self.puesto = puesto

    def crearEmpleadp():
        nombre = input("Ingresar nombre de la persona: \n")
        apellido = input("Ingresar apellido de la persona: \n")
        edad = int(input("Ingresar edad de la persona: \n"))
        dni = int(input("Ingresar dni de la persona: \n"))
        sector = input("Ingresar sector de la persona: \n")
        puesto = input("Ingresar puesto de la persona: \n")
        empleadoNuevo = Empleado(nombre, apellido, edad, dni, sector, puesto)
        print("Persona ingresada al sistema...\n")
        print(f"nombre y apellido: \n{empleadoNuevo.nombre} {empleadoNuevo.apellido}\nedad: \n{empleadoNuevo.edad}\ndni: \n{empleadoNuevo.dni}")
        print(f"n\sector y puesto: \n{empleadoNuevo.sector}/{empleadoNuevo.puesto}")
        return empleadoNuevo
    
    