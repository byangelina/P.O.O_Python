
# - Los números perfectos son aquellos que son iguales a la suma de sus propios divisores.
# - el número primo es el que solo es divisible por 1 y por si mismo (y mayor a 1).

#-----------------------------------------------------------------------------------------------

# programa de un número primo con for:
# desarrollo profe

"""
num = int(input("Ing. número :"))

contarDivisores = 0
for x in range(1, num + 1, 1):
    if num % x == 0:
        contarDivisores = contarDivisores + 1

if contarDivisores == 2:
    print("Primo")
else:
    print("No es primo")
"""



# el mismo caso pero con funciones:
# siempre, dentro de la funcion usar return, no print


def esPrimo(n):
    contarDivisores = 0
    for x in range(1, n + 1, 1):
        if n % x == 0:
            contarDivisores = contarDivisores + 1

    if contarDivisores == 2:
        return True
    else:
        return False

"""
numero = int(input("Ing. número :"))
if esPrimo(numero):
    print("primo")
else:
    print("No es primo")"""



def cantidadPrimos(c):
    contador = 0    
    numero = 1       
    string = ""  

    while contador < c:
        if esPrimo(numero):
            string += str(numero) + " "
            contador += 1
        numero += 1
    return string


inputCantidadPrimos = int(input("\nIngrese cuántos números primos desea desplegar por pantalla: "))

resultado = cantidadPrimos(inputCantidadPrimos)

print(resultado," \n")




