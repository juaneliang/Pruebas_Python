from empleado import *
from base import *

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
if(opcion==2):
    #Crear el metodo
    pass
if(opcion==3):
    #Crear el metodo
    pass
if(opcion==4):
    Base.mostrarEmpleadoBase()
if(opcion==0):
    pass