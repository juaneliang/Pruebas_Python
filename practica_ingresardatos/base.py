import sqlite3

class Base():
    pass

    def empleadoEnBase(nombre, apellido, edad, dni, sector, puesto):
        conexion = sqlite3.connect("practica_ingresardatos\databaseEmpleado.sqlite")
        cursor = conexion.cursor()
        cursor.execute(f"INSERT INTO personas (nombre, apellido, edad, dni, sector, puesto) VALUES ({nombre}, {apellido}, {edad}, {dni}, {sector}, {puesto})")
        conexion.commit()
        conexion.close()
