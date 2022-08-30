class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def crearPersona(self):
        self.nombre = input("Ingresar nombre de persona: \n")
        self.edad = input("Ingresar edad de persona: \n")
        personaCreada = Persona(self.nombre, self.edad)
        return personaCreada

    def cumpleanios(self, edad):
        self.edad += 1

#personaCreada = Persona("juan", 23)
personaCreada = Persona.crearPersona()
personaCreada.cumpleanios(personaCreada.edad)
#print("La persona agregada se llama: " + (personaCreada.nombre) + 
#"\nY cumplio: " + (personaCreada.edad) + " años.\n")
print(f"La persona agregada se llama: {personaCreada.nombre} \nY cumplio: {personaCreada.edad} años.\n")