class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def cumpleanios(self):
        self.edad += 1

personaCreada = Persona("juan", 23)
personaCreada.cumpleanios()
print(f"La persona agregada se llama: {personaCreada.nombre} \nY cumplio: {personaCreada.edad} años.\n")