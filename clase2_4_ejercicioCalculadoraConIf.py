def sumar(numero1,numero2):
    return numero1 + numero2

def restar(numero1,numero2):
    return numero1 - numero2

def multiplicar(numero1,numero2):
    return numero1 * numero2

def dividir(numero1,numero2):
    if numero2 == 0:
        resultado = "no se puede dividir por 0"
    else:
        resultado = numero1 / numero2
    return resultado

numero1 = int(input("Escribe un numero: "))

numero2 = int(input("Escribe otro numero: "))

print("el resultado de la suma es: ", sumar(numero1, numero2))
print("el resultado de la resta es: ", restar(numero1, numero2))
print("el resultado de la multiplicacion es: ", multiplicar(numero1, numero2))
print("el resultado de la division es: ", dividir(numero1, numero2))


