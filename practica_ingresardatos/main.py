from empleado import *
from base import *

conexion = sqlite3.connect("practica_ingresardatos\databaseEmpleado.sqlite")
cursor = conexion.cursor()

print("------------MENU-----------")
print("1-INGRESAR NUEVO EMPLEADO--")
print("2-MODIFICAR EMPLEADO-------")
print("3-BORRAR EMPLEADO----------")
print("4-MOSTRAR EMPLEADOS--------")
print("0-SALIR--------------------")

opcion = input("\n--INGRESAR OPCION DESEADA--\n")

if(opcion=="1"):
    empleadoNuevo = Empleado.crearEmpleado()
    empleadoNuevo.mostrarEmpleado()
elif(opcion=="2"):
    pass
elif(opcion=="3"):
    pass
elif(opcion=="4"):
    Base.mostrarEmpleadoBase()
elif(opcion=="0"):
    pass