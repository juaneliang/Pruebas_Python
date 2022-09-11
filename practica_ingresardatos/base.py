import sqlite3

from practica_ingresardatos.empleado import Empleado

class Base():

    def dameConexion():
        conexion = sqlite3.connect("practica_ingresardatos\databaseEmpleado.sqlite")
        return conexion

    def crearEmpleadoBase(nombre, apellido, edad, dni, sector, puesto):
        conexion = Base.dameConexion()
        cursor = conexion.cursor()
        cursor.execute(f"INSERT INTO empleados (nombre, apellido, edad, dni, sector, puesto) VALUES ({nombre}, {apellido}, {edad}, {dni}, {sector}, {puesto})")
        conexion.commit()
        conexion.close()

    def modificarEmpleadoBase(nombre, apellido, edad, dni, sector, puesto):
        conexion = Base.dameConexion()
        cursor = conexion.cursor()
        cursor.execute(f"INSERT INTO empleados (dni) VALUES ({dni}")
        conexion.commit()
        conexion.close()

    def borrarEmpleadoBase(dni):
        conexion = Base.dameConexion()        
        cursor = conexion.cursor()
        cursor.execute(f"INSERT INTO empleados (dni) VALUES ({dni}")
        conexion.commit()
        conexion.close()
    
    def mostrarEmpleadoBase():
        conexion = Base.dameConexion() 
        cursor = conexion.cursor()
        #refinar busqueda del select para que busque por dni
        cursor.execute(f"SELECT * FROM empleados;")
        empleado = cursor.fetchall()
        print(f"{empleado}")
        conexion.close()

    def mostrarEmpleadosBase():
        conexion = Base.dameConexion() 
        cursor = conexion.cursor()
        cursor.execute(f"SELECT * FROM empleados;")
        empleados = cursor.fetchall()
        for e in empleados:
            print(e)
        conexion.close()

 