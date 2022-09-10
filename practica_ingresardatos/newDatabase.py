import sqlite3

conexion = sqlite3.connect("practica_ingresardatos\databaseEmpleado.sqlite")
cursor = conexion.cursor()
#Se crea la tabla, si es que no existe, personas, y se agregan los parametros:
#nombre como varchar=string y edad como int
cursor.execute("CREATE TABLE IF NOT EXISTS empleados(nombre VARCHAR(20),apellido VARCHAR(30),edad INT, dni VARCHAR(9), sector VARCHAR(20), puesto VARCHAR(20))")
#Se agregan los valores "Eduardo" para nombre y 30 para edad
#cursor.execute("INSERT INTO personas (nombre, edad) VALUES ('Eduardo', 30)")
#Se hace el commit correspondiente
conexion.commit()
#Se cierra la conexion
conexion.close()