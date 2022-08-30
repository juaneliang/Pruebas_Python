class Persona:
    def __init__(self, nombre, edad):
        print("\nSe crea la persona \n")
        self.nombre = nombre
        self.edad = edad

    #def crearPersona(self, nombre, edad):
        #self.nombre = input("Ingresar nombre de persona: \n")
        #self.edad = input("Ingresar edad de persona: \n")
        #personaCreada = Persona(nombre, edad)
        #return personaCreada
    def cumpleanios(self):
        self.edad =+ 1

personaCreada = Persona("juan", 23)
personaCreada.cumpleanios()
#print("La persona agregada se llama: " + (personaCreada.nombre) + 
#"\nY cumplio: " + (personaCreada.edad) + " años.\n")
print(f"La persona agregada se llama: {personaCreada.nombre} \nY cumplio:{personaCreada.edad} años.\n")