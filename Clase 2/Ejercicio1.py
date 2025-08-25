

# primer ejercicio
print("Programa para seleccionar el número mayor de varios números")

numeromayor = 0
x = 0

while True:
    numeroinput = int(input("Ingrese un número( 0 para terminar): "))
    if numeroinput == 0:
        break
    if primer_numero:
        numeromayor = numeroinput
        primer_numero = False
    else:
        if numeroinput > numeromayor:
            numeromayor = numeroinput


# esto fue un ejemplo y esta incompleto


