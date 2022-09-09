import sqlite3

conexion = sqlite3.connect("clase4\database.sqlite")
cursor = conexion.cursor()
#Se crea la tabla, si es que no existe, personas, y se agregan los parametros:
#nombre como varchar=string y edad como int
cursor.execute("CREATE TABLE IF NOT EXISTS personas(nombre VARCHAR(45),edad INT)")
#Se agregan los valores "Eduardo" para nombre y 30 para edad
cursor.execute("INSERT INTO personas (nombre, edad) VALUES ('Eduardo', 30)")
#Se hace el commit correspondiente
conexion.commit()
#Se cierra la conexion
conexion.close()