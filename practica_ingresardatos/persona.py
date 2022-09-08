class Persona():
    def __init__(self, nombre, apellido, edad, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dni = dni

    def crearPersona():
        nombre = input("Ingresar nombre de la persona: \n")
        apellido = input("Ingresar apellido de la persona: \n")
        edad = int(input("Ingresar edad de la persona: \n"))
        dni = int(input("Ingresar dni de la persona: \n"))
        personaNueva = Persona(nombre, apellido, edad, dni)
        print("Persona ingresada al sistema...\n")
        print(f"nombre y apellido: \n{personaNueva.nombre} {personaNueva.apellido}\nedad: \n{personaNueva.edad}\ndni: \n{personaNueva.dni}")
        return personaNueva
