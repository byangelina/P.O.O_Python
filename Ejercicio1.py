
"""
def es_par(n):
    return n % 2 == 0

num = int(input("Ing. número :"))
if not es_par(num):
    print("Grabar en base datos")
else:
    print("Enviar correo al usuario que no es par")
"""



# uso de parametros en range()
"""
for i in range(start, stop, step):
    
Código a ejecutar en cada iteración

start: Número inicial (opcional, por defecto es 0).
stop: Número final (no incluido en la iteración).
step: Incremento o decremento entre valores (opcional, por defecto es 1).

"""




# - Los números perfectos son aquellos que son iguales a la suma de sus divisores propios
# - el número primo es el que solo es divisible por 1 y por si mismo

# programa de un número primo con for:
# caso profe

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
# dentro de la funcion usar return, no print

def esPrimo(n):
    contarDivisores = 0
    for x in range(1, n + 1, 1):
        if n % x == 0:
            contarDivisores = contarDivisores + 1

    if contarDivisores == 2:
        return True
    else:
        return False
#_______________________________________________________

numero = int(input("Ing. número :"))
if esPrimo(numero):
    print("primo")
else:
    print("No es primo")





























