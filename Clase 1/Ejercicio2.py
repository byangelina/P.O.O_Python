"""
desarrolle un programa que solicite un numero al usuario y despliegue la siguiente serie.

Ejemplo: el usuario ingresa un "10".
1
12
123
1234
12345
"""

numero_ingresado = input(int("Ingrese un número: "))

num = 0

for i in range (10):
    if num >= numero_ingresado:
        num += 1
    break






