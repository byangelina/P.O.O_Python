
# listas: mutables []
# tuplas: imutables {}
# prox. clase: investigar listas y métodos de listas, diferentes ejercicios.




# realice un programa que le pida al usuario que le solicite al usuario cuantos numero primos desea desplegar por pantalla
# el sistema desplegara la cantidad partiendo por el numero 1

# la funcions se debe llamar cantidadPrimos(c) recibe un argumento c y retorna un String:

# def cantidadPrimos(c)
#   return "texto"

inputCantidadPrimos = int(input("Ingrese cuántos número primos desea desplegar por pantalla: "))

def esPrimo(n):
    contarDivisores = 0
    for x in range(1, n + 1, 1):
        if n % x == 0:
            contarDivisores = contarDivisores + 1

    if contarDivisores == 2:
        return True
    else:
        return False

def cantidadPrimos(c):
    if c == esPrimo:
        inputCantidadPrimos == c +1
        inputCantidadPrimos = str

    else:
        inputCantidadPrimos == c +1
        inputCantidadPrimos = str

if inputCantidadPrimos(c):
    print("a")
else:
    print("b")


# resolver antes de las 12 de la noche



