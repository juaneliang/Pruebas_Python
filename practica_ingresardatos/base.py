import sqlite3

conexion = sqlite3.connect("practica_ingresardatos\databaseEmpleado.sqlite")
cursor = conexion.cursor()

class Base():
    pass

    def crearEmpleadoBase(nombre, apellido, edad, dni, sector, puesto):
        cursor.execute(f"INSERT INTO empleados (nombre, apellido, edad, dni, sector, puesto) VALUES ({nombre}, {apellido}, {edad}, {dni}, {sector}, {puesto})")
        conexion.commit()
        conexion.close()

    def modificarEmpleadoBase(nombre, apellido, edad, dni, sector, puesto):
        cursor.execute(f"INSERT INTO empleados (nombre, apellido, edad, dni, sector, puesto) VALUES ({nombre}, {apellido}, {edad}, {dni}, {sector}, {puesto})")
        conexion.commit()
        conexion.close()

    def borrarEmpleadoBase(dni):
        cursor.execute(f"INSERT INTO empleados (dni) VALUES ({dni}")
        conexion.commit()
        conexion.close()

    def mostrarEmpleadoBase():
        cursor.execute(f"SELECT * FROM empleados")
        conexion.commit()
        conexion.close()