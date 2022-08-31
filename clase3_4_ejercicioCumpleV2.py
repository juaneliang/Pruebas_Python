class Persona:
    def __init__(self, nombre, edad):
        print("\nPersona creada\n")
        self.nombre = nombre
        self.edad = edad

    def agregarPersona():
        nombre = input("\nIngresar nombre de la persona: ")
        edad = int(input("\nIngresar edad de la persona: "))
        persona = Persona(nombre, edad)
        return persona

    def cumpleanios(self):
        self.edad += 1

    def mostrarPersona(personaCreada):
        print(f"La persona agregada se llama: {personaCreada.nombre} \nY cumplio: {personaCreada.edad} años.\n")

personaCreada = Persona.agregarPersona()
personaCreada.cumpleanios()
personaCreada.mostrarPersona()
#print(f"La persona agregada se llama: {personaCreada.nombre} \nY cumplio: {personaCreada.edad} años.\n")